from data.data import *
from static.var import *
from static.caminhos import *
from modules.api.sftp import *
from modules.api.email import *
from modules.api.api_crm import *
from modules.api.api_vendas import *
from modules.api.api_contas import *
from modules.funcs.geradores import *
from modules.api.api_produtos import *
from modules.api.api_clientes import *
from modules.funcs.operadores import *
from modules.api.api_projetos import *
from datetime import datetime, timedelta
from modules.api.api_fornecedores import *


#NOTE - get_vendas
def get_vendas(data_inicio, data_final):
    """
    Retrieves sales data.

    Returns:
        list: A list of dictionaries containing the sales data.
    """
    pass

#NOTE - get_produtos
def get_produtos(dados_venda: list, dados_produtos_fornecedores: dict):
    """
    Retrieves detailed product information based on a list of sales data.

    Args:
        dados_venda (list): A list containing sales data.
        dados_produtos_fornecedores (dict): A dictionary containing supplier product data.

    Returns:
        list: A list of dictionaries containing detailed product information.
    """
    pass

#NOTE - set_caracteristicas_produtos
def set_caracteristicas_produtos(dados_produtos: list):
    """
    Sets the product features.

    Args:
        dados_produtos (list): A list containing product data.
    """
    pass

#NOTE - get_produtos_fornecedores
def get_produtos_fornecedores():
    """
    Retrieves the data of products and suppliers.

    Returns:
        list: A list of dictionaries containing the data of products and suppliers.
        Each dictionary has a key that represents the trade name of the supplier
        and a value that represents the supplier's CPF/CNPJ.
    """
    pass

#NOTE - get_clientes
def get_clientes(dados_vendas: list, dados_projetos: dict):
    """
    Retrieves client data based on sales data.

    Args:
        dados_vendas (list): A list of dictionaries containing sales data.

    Returns:
        list: A list of dictionaries containing client data.
    """
    pass

#NOTE - get_medicos_crm
def get_medicos_crm():
    """
    Retrieves the CRM of the doctors.

    Returns:
        dict: A dictionary containing the names of doctors as keys and their respective CRM as values.
    """
    pass

#NOTE - set_registro_profissional
def set_registro_profissional(dados_clientes: list, medicos_crm: dict):
    """
    Updates the clients' professional registration data based on the doctors' data.

    Args:
        dados_clientes (list): A list containing client data.
        medicos_crm (dict): A dictionary containing the doctors' data, where the keys are the names of the doctors
                            and the values are the professional registration data.

    Returns:
        list: The updated list with the clients' professional registration data.
    """
    pass

#NOTE - get_projetos
def get_projetos():
    """
    Returns a dictionary containing project data.

    Returns:
        dict: A dictionary containing the project codes as keys and the project names as values.
    """
    pass

#NOTE - get_usuarios
def get_usuarios():
    """
    Retrieves user emails through the function listar_usuarios.

    Returns:
        list: List containing user emails.
    """
    pass

#SECTION - main_script
def main_script(data_inicio: str, data_final: str):
    """
    Main function that executes the script to generate demand reports.

    Returns:
        tuple: A tuple containing the destination file name and the list of names of the reports generated.
    """
    pass

#SECTION - enviar_relatorios
def enviar_relatorios_iqvia(nome_arquivo_destino: str, lista_relatorios: list):
    """
    Sends the demand reports via email and SFTP.

    Args:
        nome_arquivo_destino (str): The destination file name.
        lista_relatorios (list): A list containing the names of the reports to be sent.
    """
    pass
