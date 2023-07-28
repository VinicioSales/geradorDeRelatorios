from os import getenv
from dotenv import load_dotenv
from errors.error_handler import *

load_dotenv()

try:
    credendiais = {
        "app_key": getenv("APP_KEY"),
        "app_secret": getenv("APP_SECRET"),
        "senha_email": getenv("SENHA_EMAIL"),
        "codigo_iqvia": getenv("CODIGO_IQVIA"),
        "host_iqvia": getenv("HOST_IQVIA"),
        "login_iqvia": getenv("LOGIN_IQVIA"),
        "senha_iqvia": getenv("SENHA_IQVIA")
    }
except Exception as erro:
    error_handler(erro=erro, local="credendiais")
    set_log_usuario(mensagem="Ocorreu um erro ao buscar os credenciais. Por favor, entre em contato com o suporte para obter assistência.")
    raise


dados_empresa = {
    "razao_social_empresa": "Oito Pharma Medicamentos e Produtos Para Saude LTDA",
    "cnpj_empresa": "29.293.582-0001-23",
    "email_destino": getenv("EMAIL_DESTINO"),
}

try:
    script_data = {
        "email_parceiro": getenv("EMAIL_PARCEIRO"),
        "senha_email_parceiro": getenv("SENHA_EMAIL_PARCEIRO"),
        "url_server": getenv("URL_SERVER")
    }
except Exception as erro:
    error_handler(erro=erro, local="script_data")
    set_log_usuario(mensagem="Ocorreu um erro ao buscar os dados do script. Por favor, entre em contato com o suporte para obter assistência.")
    raise
