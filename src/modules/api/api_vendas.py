import json
import datetime
from requests import request
from data.data import credendiais
from errors.error_handler import *

app_key = credendiais['app_key']
app_secret = credendiais['app_secret']

url = 'https://app.omie.com.br/api/v1/produtos/pedido/'

#NOTE - listar_pedidos
def listar_pedidos(data_inicio: str, data_final: str, pagina: int):
    """Requisita a lista de pedidos de vendas.

    Parâmetros:
        - pagina: int - O número da página desejada na lista de pedidos.

    Retorno:
        - response - O objeto de resposta contendo os dados da lista de vendas."""
    payload = json.dumps({
        'call': 'ListarPedidos',
        'app_key': app_key,
        'app_secret': app_secret,
        'param': [
            {
                "pagina": pagina,
                "registros_por_pagina": 500,
                "apenas_importado_api": "N",
                "status_pedido": "FATURADO",
                "filtrar_por_data_de": data_inicio,
                "filtrar_por_data_ate": data_final
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
            set_log_usuario(mensagem="Ocorreu um erro ao buscar as vendas. Por favor, entre em contato com o suporte para obter assistência.")
            error_handler(local="listar_pedido", erro=response.json())
            raise
    except Exception as erro:
        error_handler(erro=erro)
        set_log_usuario(mensagem="Ocorreu um erro ao buscar as vendas. Por favor, entre em contato com o suporte para obter assistência.")
        raise
