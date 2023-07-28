import inspect
import traceback
from logging import basicConfig
from logging import INFO
from modules.log.log_config import * 

basicConfig(level=INFO)

#NOTE - error_handler
def error_handler(erro, local=None):
    if isinstance(erro, Exception):
        current_error = erro
        while current_error:
            print(f'current_error: {current_error}')
            tb_list = traceback.extract_tb(current_error.__traceback__)
            error_name = type(current_error).__name__
            error_message = str(current_error)
            for frame in reversed(tb_list):
                filename = frame.filename
                lineno = frame.lineno
                logger_log.error(f"{error_name}: {error_message} in {filename} at line {lineno}")
            current_error = current_error.__cause__
        logger_log.info("-------------------------------------------------------------------------------------")
    else:
        logger_log.error(f"{local} - {erro}")

def set_log_usuario(mensagem: str):
    logger_usuario.error(f"{mensagem}! Contate o suporte.")

#NOTE - validar_tamanho_dado
def validar_tamanho_dado(tipo: str, dado: any, tamanho_total_string: int):
    # Get caller information
    caller_frame = inspect.stack()[1]
    caller_filename = caller_frame.filename
    caller_lineno = caller_frame.lineno

    if len(dado) > tamanho_total_string:
        logger_usuario.error(msg=f"O número de caracteres de {tipo} excede {tamanho_total_string}")
        logger_usuario.error(msg=f"called from {caller_filename} at line {caller_lineno}")
        logger_usuario.info("-------------------------------------------------------------------------------------")
        return False
    
    return True

