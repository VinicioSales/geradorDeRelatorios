from data.data import *
from .operadores import *
from .utilidades import *
from datetime import datetime, date

data_arquivo = data_atual = datetime.now().strftime("%d%m%Y")
data_arquivo = manter_apenas_numeros(texto=data_arquivo)


#SECTION - get_relatorio_demanda_cliente
def get_relatorio_demanda_cliente(dados_cliente: list, data_inicio: datetime, data_final: datetime):
    """
    Generates a customer demand report based on the provided data.

    Args:
        dados_cliente (list): A list containing the client data.
        data_inicio (datetime): The start date of the report period.
        data_final (datetime): The end date of the report period.

    Returns:
        str: The name of the generated report file.
    """
    pass
#!SECTION

#SECTION - get_relatorio_demanda_produtos
def get_relatorio_demanda_produtos(dados_produtos: list, data_inicio: datetime, data_final: datetime):
    """
    Generates a product demand report based on the provided data.

    Args:
        dados_produtos (list): A list containing the product data.
        data_inicio (datetime): The start date of the report period.
        data_final (datetime): The end date of the report period.

    Returns:
        str: The name of the generated report file.
    """
    pass
#!SECTION

#SECTION - get_relatorio_demanda_vendas
def get_relatorio_demanda_vendas(dados_vendas: list, data_inicio: datetime, data_final: datetime):
    """
    Generates a sales demand report based on the provided data.

    Args:
        dados_vendas (list): A list containing the sales data.
        data_inicio (datetime): The start date of the report period.
        data_final (datetime): The end date of the report period.

    Returns:
        str: The name of the generated report file.
        str: id_periodo
    """
    pass
#!SECTION
