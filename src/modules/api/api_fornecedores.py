import json
from requests import request
from data.data import credendiais
from errors.error_handler import *

app_key = credendiais['app_key']
app_secret = credendiais['app_secret']
url = "https://app.omie.com.br/api/v1/estoque/produtofornecedor/"

#NOTE - listar_produto_fornecedor
def listar_produto_fornecedor(pagina: int):
    payload = json.dumps({
        'call': 'ListarProdutoFornecedor',
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
            set_log_usuario(mensagem="Ocorreu um erro ao buscar os fornecedores. Por favor, entre em contato com o suporte para obter assistência.")
            error_handler(local="listar_produto_fornecedor", erro=response.json())
            raise SystemExit
    except Exception as erro:
        error_handler(erro=erro)
        set_log_usuario(mensagem="Ocorreu um erro ao buscar os fornecedores. Por favor, entre em contato com o suporte para obter assistência.")
        raise
