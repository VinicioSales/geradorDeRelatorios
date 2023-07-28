import smtplib
from data.data import *
from static.caminhos import *
from modules.api.email import *
from errors.error_handler import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


email_destino = dados_empresa["email_destino"]
email_parceiro = script_data["email_parceiro"]
senha_email_parceiro = script_data["senha_email_parceiro"]


def enviar_email(email_destino: str, assunto: str, email_remetente: str, senha: str, anexo=None, mensagem=None):
    """
    Envia um email para o destinatário com arquivos anexados
    
    Args:
        email_destino (str): email de destino
        assunto (str): assunto do email
        email_remetente (str)
        senha (str)
        anexos (list): lista de caminhos de arquivos a serem anexados
    """
    try:
        msg = MIMEMultipart()
        msg['Subject'] = assunto
        msg['From'] = email_remetente
        msg['To'] = email_destino
        
        if mensagem != None:
            msg.attach(MIMEText(mensagem, "plain"))

        if anexo != None:
            with open(anexo, "rb") as f:
                attach = MIMEApplication(f.read(), _subtype="txt")
                attach.add_header('content-disposition', 'attachment', filename=anexo)
                msg.attach(attach)

        # Conectar ao servidor SMTP e enviar o e-mail
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.starttls()
            s.login(email_remetente, senha)
            s.sendmail(email_remetente, [email_destino], msg.as_string().encode('utf-8'))

        print('Email enviado!')
    except Exception as erro:
        print(erro)
        error_handler(erro=erro)
        set_log_usuario(mensagem="Ocorreu um erro ao enviar para o e-mail destino. Por favor, entre em contato com o suporte para obter assistência.")
        raise

