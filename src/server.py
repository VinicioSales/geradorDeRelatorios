import os
import secrets
from flask_cors import CORS
from modules.funcs.operadores import *
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request as rq, jsonify, session, url_for
from flask_login import UserMixin, LoginManager, login_user, login_manager, current_user, login_required, logout_user
from data.data import *

url_server = script_data["url_server"]


#NOTE - Instâncias
app = Flask(__name__)
CORS(app)
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=1)


#NOTE - Configuração
login_manager = LoginManager()
login_manager.init_app(app=app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
app.secret_key = os.urandom(24)

#NOTE - Tabela
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    senha = db.Column(db.String(80), nullable=False)
    ultimo_login = db.Column(db.DateTime)
    token_recuperacao_senha = db.Column(db.String(6))
    token_confirmar_registro = db.Column(db.String(6))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()

#NOTE - index
@app.route("/", methods=["GET"])
def index():
    if current_user.is_authenticated:
        if datetime.utcnow() - current_user.ultimo_login > timedelta(hours=24):
            return render_template("login.html")
        return render_template("index.html")
    else:
        return render_template("login.html")

#NOTE - enviar_relatorios
@login_required
@app.route("/enviar_relatorios", methods=["POST"])
def enviar_relatorios():
    print("requisitado enviar_relatorios")
    dados = rq.get_json()
    data_inicio = dados.get("dataInicio", None)
    data_final = dados.get("dataFinal", None)
    nome_arquivo_destino, lista_relatorios = main_script(data_inicio=data_inicio, data_final=data_final)
    enviar_relatorios_iqvia(nome_arquivo_destino=nome_arquivo_destino, lista_relatorios=lista_relatorios)

    return jsonify(message=200)

#NOTE - registrar
@login_required
@app.route("/registrar", methods=["POST", "GET"])
def registrar():
    emails_usuarios = get_usuarios()
    print(f'emails_usuarios: {emails_usuarios}')
    if rq.method == "POST":
        dados = rq.get_json()
        email = dados["email"]
        senha = dados["senha"]

        emails_usuarios = get_usuarios()
        if email not in emails_usuarios:
            return jsonify({"message": f"Cadastro não permitido", "redirect": f"{url_for('registrar')}"}), 200

        usuario = User.query.filter_by(email=email).first()
        if usuario != None:
            if usuario.token_confirmar_registro == None:
                return jsonify({"message": "E-mail já cadastrado!"}), 409
            else:
                return jsonify({"message": "E-mail aguardando confirmação!"}), 409

        novo_usuario = User(email=email, senha=generate_password_hash(senha, method="sha256"))
        token = secrets.token_hex(3)
        novo_usuario.token_confirmar_registro = token
        db.session.add(novo_usuario)
        db.session.commit()
        mensagem = email_confirmar_email(link=f"{url_server}/confirmar_email", token=token)
        enviar_email(email_destino=novo_usuario.email, assunto="Confirmação de Email - Ação Necessária", email_remetente=email_parceiro, senha=senha_email_parceiro, mensagem=mensagem)


        return jsonify({"message": f"E-mail de confirmação enviado para o e-mail: {email}, redirect': {url_for('confirmar_email')}"}), 200
    return render_template("cadastro.html")

#NOTE - confirmar_email
@app.route("/confirmar_email", methods=["POST", "GET"])
def confirmar_email():
    if rq.method == "POST":
        token = rq.get_json().get("token")
        usuario = User.query.filter_by(token_confirmar_registro=token).first()
        if usuario is not None:
            usuario.token_confirmar_registro = None
            db.session.commit()

            return jsonify({"message": f"Registro feito com sucesso!", "redirect": url_for("login")}), 200
    
        return jsonify({"message": f"Token inváldo"}), 401
    
    return render_template("confirmar_email.html")

#NOTE - login
@app.route("/login", methods=["POST", "GET"])
def login():
    emails_usuarios = get_usuarios()
    print(f'emails_usuarios: {emails_usuarios}')
    if rq.method == "POST":
        dados = rq.get_json()
        email = dados["email"]
        senha = dados["senha"]

        if email not in emails_usuarios:
            return jsonify({"message": f"Login não permitido", "redirect": f"{url_for('login')}"}), 200

        usuario = User.query.filter_by(email=email).first()
        if usuario and usuario.token_confirmar_registro is not None:
            return jsonify({"message": "E-mail esperando confirmação!", "status": 401})

        elif usuario and check_password_hash(usuario.senha, senha):
            usuario.ultimo_login = datetime.utcnow()
            db.session.commit()
            login_user(usuario)
            session.permanent = True
            return jsonify({"redirect": url_for("index"), "status": 200})
        
        return jsonify({"message": "Usuário não encontrado!", "status": 401})

    return render_template("login.html"), 200

#NOTE - logout
@app.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return jsonify({"redirect": url_for("login")}), 200

#NOTE - recuperar_senha
@app.route("/recuperar_senha", methods=["POST", "GET"])
def recuperar_senha():
    if rq.method == "POST":
        email = rq.get_json().get("email")
        usuario = User.query.filter_by(email=email).first()
        if usuario != None:
            token = secrets.token_hex(3)
            usuario.token_recuperacao_senha = token
            db.session.commit()
            
            mensagem = email_recuperar_senha(token=token, url=url_server)

            enviar_email(email_destino=usuario.email, assunto="Recuperar senha", email_remetente=email_parceiro, senha=senha_email_parceiro, mensagem=mensagem)
            
            return jsonify({"message": f"Token de recuperação enviado para o e-mail {email}"}), 200
        else:
            return jsonify({"message": "e-mail não cadastrado"}), 404

#NOTE - redefinir_senha
@app.route("/redefinir_senha", methods=["POST", "GET"])
def redefinir_senha():
    if rq.method == "POST":
        senha = rq.get_json().get("senha")
        token = rq.get_json().get("token")

        
        usuario = User.query.filter_by(token_recuperacao_senha=token).first()
        if usuario != None:
            usuario.senha = generate_password_hash(senha, method="scrypt")
            usuario.token_recuperacao_senha = None
            db.session.commit()

            return jsonify({"redirect": url_for("index"), "message": "Senha redefinida com sucesso!"}), 200
        else:
            return jsonify({"message": "Token inválido!"}), 400
    
    return render_template("redefinir_senha.html")


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8000)
