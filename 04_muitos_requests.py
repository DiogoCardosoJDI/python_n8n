import requests
from pprint import pprint

def obter_requests(url, params=None):
    #Faz requisição get e retorna json

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    except requests.HTTPError as e:
        print(f"Erro no reuqest - {e}")
        return None
    
def busca_id_estado():
    #Obtemn um dicionario de estados no formato {id_estado: nome_estado}
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"

    dados_estados = obter_requests(url, params={"view": "nivelado"}) or []
    
    return {estado["UF-id"]: estado["UF-nome"] for estado in dados_estados}


def frequencia_nome(nome):
    #Obtem um dicionario de frequencia de um nome por estado no formato {id_estado: frequencia}
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"

    dados_frequencia = obter_requests(url, params={"groupBy": "UF"}) or []
                                                   
    return {int(dado["localidade"]): dado["res"][0]["proporcao"] for dado in dados_frequencia}

def main(nome):
    dict_estado = busca_id_estado()
    dict_frequencias = frequencia_nome(nome)
    pprint(dict_estado)
    pprint(dict_frequencias)

    print(f"=== Frequencia do nome {nome} nos Estados por 100.00 habitantes ===")

    for id_estado, frequencia in sorted(dict_frequencias.items(), key=lambda item: item[1], reverse=True):
        print(f"-> {dict_estado.get(id_estado, 'Desconhecido')}: {frequencia}")

if __name__ == "__main__":
    main("braulio")