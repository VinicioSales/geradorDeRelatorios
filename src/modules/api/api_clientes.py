import json
from requests import request
from data.data import credendiais
from errors.error_handler import *

app_key = credendiais['app_key']
app_secret = credendiais['app_secret']
url = "https://app.omie.com.br/api/v1/geral/clientes/"

def listar_clientes(pagina: int):
    payload = json.dumps({
        'call': 'ListarClientes',
        'app_key': app_key,
        'app_secret': app_secret,
        'param': [
            {
                    "pagina": pagina,
                    "registros_por_pagina": 500

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
            set_log_usuario(mensagem="Ocorreu um erro ao buscar os clientes. Por favor, entre em contato com o suporte para obter assistência.")
            error_handler(local="listar_clientes", erro=response.json())
            raise
    except Exception as erro:
        error_handler(erro=erro)
        set_log_usuario(mensagem="Ocorreu um erro ao buscar os clientes. Por favor, entre em contato com o suporte para obter assistência.")
        raise
