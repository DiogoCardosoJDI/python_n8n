from pprint import pprint
import requests

nome = input("Digite o nome para pesquisa:\n\n")

url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"

params = {
    "localidade": 33 #RJ
}

response = requests.get(url, params=params)

try:
    response.raise_for_status()
except requests.HTTPError as e:
    print(f"Erro no request: {e}")
    resultado = None
else:
    resultado = response.json()
    #print(resultado)
    pprint(resultado[0]["res"])