import re
import zipfile
from static.caminhos import *
from unidecode import unidecode
from modules.api.api_vendas import *
from modules.api.api_produtos import *



#NOTE - zip_arquivo 
def zip_arquivo(arquivos_origem: list, arquivo_destino: str):
    """
    Compresses source files into a destination zip file.

    Args:
        arquivos_origem (list): List of source file paths.
        arquivo_destino (str): Path to the destination zip file.

    """
    pass

#NOTE - set_espaco_branco
def set_espaco_branco(texto: str, direcao: str, tamanho_total_string: int):
    """Adds white spaces to the left or right of a text.

    Args:
        texto (str): The text to which the white spaces will be added.
        direcao (str): The direction in which the white spaces will be added. Should be 'left' or 'right'.
        tamanho_total_string (int): The total length of white spaces to be added.

    Returns:
        str: The resulting text with the added white spaces.
    """
    pass

#NOTE - remover_caracteres_especiais
def manter_apenas_numeros(texto: str):
    """
    Removes special characters from a CNPJ.

    Args:
        str (str): the string to be formatted.

    Returns:
        str: The string without special characters.

    """
    pass

#NOTE - manter_apenas_numeros_letras
def manter_apenas_numeros_letras(texto: str):
    """
    Removes characters that are not letters and numbers

    Args:
        str (str): the string to be formatted.

    Returns:
        str: The string without special characters.

    """
    pass

#NOTE - set_zeros_esquerda
def set_zeros_esquerda(texto: str, tamanho_total_string: int):
    """
    Adds zeros to the left of a string to reach a specific total size.

    Args:
        texto (str): The original string.
        tamanho_total_string (int): The desired total size of the string after adding zeros.

    Returns:
        str: The resulting string after adding zeros to the left.
    """
    pass

#NOTE - tratar_dados
def tratar_dados(lista_dados: list):
    """
    Performs data treatment on a list of dictionaries.

    Iterates over the dictionaries in the list and applies the following transformations:
    - Applies the `unidecode` function to remove accents and special characters from each dictionary value.
    - Converts the resulting values to uppercase.

    Args:
        lista_dados (list): A list containing dictionaries to be treated.

    Returns:
        list: The list of dictionaries after data treatment.
    """
    pass


#NOTE - email_recuperar_senha
def email_recuperar_senha(token: str, url:str):
    return f"""
Olá,
Recebemos uma solicitação de recuperação de senha para a sua conta. Para prosseguir com o processo de recuperação, utilize o token abaixo como destaque:


Token de Recuperação: {token}


Caso você não tenha solicitado essa recuperação de senha ou acredite que tenha recebido este email por engano, por favor, entre em contato conosco imediatamente.
Para redefinir sua senha, siga as instruções abaixo:

Acesse a página de recuperação de senha no nosso site: {url}/redefinir_senha/{token}.
Insira o seu endereço de email associado à sua conta.
Digite o token de recuperação destacado acima.
Siga as instruções na página para redefinir sua senha.
Se você tiver qualquer dúvida ou precisar de assistência adicional, nossa equipe de suporte estará pronta para ajudar.
Lembramos que é importante manter sua senha segura e não compartilhá-la com ninguém. Recomendamos também que você escolha uma senha forte, contendo uma combinação de letras maiúsculas e minúsculas, números e caracteres especiais.
Agradecemos a sua compreensão e colaboração.
"""

#NOTE - email_confirmar_email
def email_confirmar_email(link: str, token: str):
    return f"""
Olá,

Obrigado por criar uma conta conosco! Para garantir que o endereço de email fornecido esteja correto, precisamos confirmá-lo.

Para confirmar o seu email, siga os passos abaixo:

Clique no link a seguir ou copie e cole-o na barra de endereços do seu navegador: {link}

Insira o token de confirmação fornecido abaixo quando solicitado:

Token de Confirmação: {token}

Ao clicar no link e inserir o token de confirmação, você estará ativando sua conta e poderá aproveitar todos os recursos e benefícios que oferecemos.

Caso você não tenha criado uma conta conosco ou acredite que recebeu este email por engano, por favor, entre em contato imediatamente para que possamos resolver a situação.

Agradecemos por se juntar à nossa comunidade e estamos ansiosos para proporcionar uma ótima experiência a você. Se tiver alguma dúvida ou precisar de suporte, não hesite em nos contatar.
"""
