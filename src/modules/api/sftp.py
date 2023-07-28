import pysftp
from data.data import *
from static.caminhos import *
from modules.api.email import *
from errors.error_handler import *

email_destino = dados_empresa["email_destino"]
email_parceiro = script_data["email_parceiro"]
senha_email_parceiro = script_data["senha_email_parceiro"]


#NOTE - enviar_arquivo_para_sftp
def enviar_arquivo_para_sftp(host: str, username: str, password: str, local_filepath: str, remote_filepath: str):
    """
    Envia um arquivo para um servidor SFTP.

    Args:
        host (str): O endereço do servidor SFTP.
        username (str): O nome de usuário para autenticação no servidor SFTP.
        password (str): A senha para autenticação no servidor SFTP.
        local_filepath (str): O caminho local do arquivo a ser enviado.
        remote_filepath (str): O caminho remoto do arquivo no servidor SFTP.
    """
    try:
        cnopts = pysftp.CnOpts()
        #FIXME - VERIFICAR VERIFICAÇÃO CHAVE HOST
        cnopts.hostkeys = None  # Desabilita a verificação de chave do host

        with pysftp.Connection(host, username=username, password=password, cnopts=cnopts) as sftp:
            sftp.put(local_filepath, remote_filepath)

        print("Arquivo enviado com sucesso.")
    except Exception as erro:
        error_handler(erro=erro)
        set_log_usuario(mensagem="Ocorreu um erro ao enviar o relatório para o IQVIA. Por favor, entre em contato com o suporte para obter assistência.")
        raise

