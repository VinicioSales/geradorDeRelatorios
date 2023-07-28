import json
from typing import Union
from requests import request
from data.data import credendiais
from errors.error_handler import *

app_key = credendiais['app_key']
app_secret = credendiais['app_secret']

url = 'https://app.omie.com.br/api/v1/geral/produtos/'

#NOTE - listar_produtos
def listar_produtos(pagina):
    """Retorna uma lista de produtos.

    Parâmetros:
    - pagina: int - O número da página desejada na lista de produtos.

    Retorno:
    response - O objeto de resposta contendo os dados da lista de produtos."""
    payload = json.dumps({
        'call': 'ListarProdutos',
        'app_key': app_key,
        'app_secret': app_secret,
        'param': [
            {
                    "pagina": pagina,
                    "registros_por_pagina": 500,
                    "apenas_importado_api": "N",
                    "filtrar_apenas_omiepdv": "N"

            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = request(method='POST', url=url, headers=headers, data=payload)
        if response.status_code == 200:
            return response.json()
        else:
            set_log_usuario(mensagem="Ocorreu um erro ao buscar os produtos. Por favor, entre em contato com o suporte para obter assistência.")
            error_handler(local="listar_produtos", erro=response.json())
            raise
    except Exception as erro:
        error_handler(erro=erro)
        set_log_usuario(mensagem="Ocorreu um erro ao buscar os produtos. Por favor, entre em contato com o suporte para obter assistência.")
        raise

#NOTE - consultar_prduto
def consultar_prduto(codigo_produto: Union[str, int]):
    """
    Consulta um produto com base no código informado.

    Args:
        codigo_produto (Union[str, int]): O código do produto a ser consultado.

    Returns:
        Union[Dict[str, Any], None]: Um dicionário contendo as informações do produto consultado, ou None se ocorrer um erro.

    Raises:
        Exception: Se ocorrer um erro ao fazer a consulta.

    """
    payload = json.dumps({
        'call': 'ConsultarProduto',
        'app_key': app_key,
        'app_secret': app_secret,
        'param': [
            {
                "codigo_produto": codigo_produto
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = request(method='POST', url=url, headers=headers, data=payload)
        if response.status_code == 200:
            return response.json()
        else:
            set_log_usuario(mensagem="Ocorreu um erro ao consultar o produtos. Por favor, entre em contato com o suporte para obter assistência.")
            error_handler(local="consultar_prduto", erro=response.json())
            raise
    except Exception as erro:
        error_handler(erro=erro)
        set_log_usuario(mensagem="Ocorreu um erro ao consultar o produtos. Por favor, entre em contato com o suporte para obter assistência.")
        raise
