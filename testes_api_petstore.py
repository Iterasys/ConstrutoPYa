import pytest
import requests

url = 'https://petstore.swagger.io/v2/user'

def testar_incluir_usuario():
    # Configura
    status_code_esperado = 200      # comunicação
    codigo_esperado = 200           # funcional
    tipo_esperado = 'unknown'       # fixo como desconhecido
    mensagem_esperada = '12181'     # id do usuário

    headers = {'Content-Type': 'application/json'}

    # Executa
    resposta = requests.post(url=url,
                             data=open('json/usuario1.json', 'rb'),
                             headers=headers
                             )
    corpo_da_resposta = resposta.json()
    print(resposta) # Status Code
    print(resposta.status_code) # Status Code
    print(corpo_da_resposta) # Response Body / Corpo da Resposta

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada

def testar_consultar_usuario():
    # Configura
    username = 'correia' # input / entrada para a consulta
    id_esperado = 12181
    username_esperado = 'correia'
    email_esperado = 'test@iterasys.com.br'
    telefone_esperado = '11999992181'
    user_status_esperado = 0
    status_code_esperado = 200      # comunicação

    headers = {'Content-Type': 'application/json'}

    # Executa
    resposta = requests.get(f'{url}/{username}', headers=headers)

    corpo_da_resposta = resposta.json()
    print(resposta) # Status Code
    print(resposta.status_code) # Status Code
    print(corpo_da_resposta) # Response Body / Corpo da Resposta

    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['id'] == id_esperado
    assert corpo_da_resposta['username'] == username_esperado
    assert corpo_da_resposta['email'] == email_esperado
    assert corpo_da_resposta['phone'] == telefone_esperado
    assert corpo_da_resposta['userStatus'] == user_status_esperado