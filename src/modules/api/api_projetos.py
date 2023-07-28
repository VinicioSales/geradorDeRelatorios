import json
import datetime
from requests import request
from data.data import credendiais
from errors.error_handler import *

app_key = credendiais['app_key']
app_secret = credendiais['app_secret']

url = 'https://app.omie.com.br/api/v1/geral/projetos/'

#NOTE - listar_projetos
def listar_projetos(pagina):
    """
    Lista os projetos com base na página especificada.

    Args:
        pagina (int): O número da página a ser consultada.

    Returns:
        Union[Dict[str, Any], None]: Um dicionário contendo os projetos encontrados na página especificada, ou None se ocorrer um erro.
    """
    data_atual = datetime.date.today()
    data_atual = data_atual.strftime("%d/%m/%Y")
    payload = json.dumps({
        'call': 'ListarProjetos',
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
            set_log_usuario(mensagem="Ocorreu um erro ao buscar os projetos. Por favor, entre em contato com o suporte para obter assistência.")
            error_handler(local="listar_projetos", erro=response.json())
            raise
    except Exception as erro:
        error_handler(erro=erro)
        set_log_usuario(mensagem="Ocorreu um erro ao buscar os projetos. Por favor, entre em contato com o suporte para obter assistência.")
        raise
