import pytest
import requests
import json

def testar_incluir_usuario():


    resposta = requests.post('https://petstore.swagger.io/v2/user')