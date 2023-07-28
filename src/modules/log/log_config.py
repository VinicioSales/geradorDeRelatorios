import os
import logging
from static import caminhos





logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

handler_usuario = logging.FileHandler(f'{caminhos.log}/log_usuario.log', encoding='utf-8')
handler_usuario.setLevel(logging.INFO)
handler_relatorio = logging.FileHandler(f'{caminhos.log}/log_relatorio.log', encoding='utf-8')
handler_relatorio.setLevel(logging.INFO)
handler_log = logging.FileHandler(f'{caminhos.log}/log.log', encoding='utf-8')
handler_log.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler_usuario.setFormatter(formatter)
handler_relatorio.setFormatter(formatter)
handler_log.setFormatter(formatter)

logger_usuario = logging.getLogger("usuario")
logger_usuario.addHandler(handler_usuario)
logger_relatorio = logging.getLogger("relatorio")
logger_relatorio.addHandler(handler_relatorio)
logger_log = logging.getLogger("log")
logger_log.addHandler(handler_log)

