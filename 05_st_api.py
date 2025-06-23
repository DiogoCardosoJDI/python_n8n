import requests
import pandas as pd
import streamlit as st

def obter_requests(url, params=None):
    #Faz requisição get e retorna json

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    except requests.HTTPError as e:
        print(f"Erro no reuqest - {e}")
        return None
    
def frequencia_nome(nome):
    #Obtem um dicionario de frequencia de um nome por decada no formato {decada: quantidade}
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"

    dados_nome = obter_requests(url) or []
                                                   
    dados_dict = {dado["periodo"]: dado["frequencia"] for dado in dados_nome[0].get("res",[])}

    df = pd.DataFrame.from_dict(dados_dict, orient="index")
    return df
    #return {dado["periodo"]: dado["frequencia"] for dado in dados_nome[0].get("res",[])}

def main():
    st.title("Web App API")
    st.header("Dados da API IBGE")
    inp_nome = st.text_input("Digite um nome:\n")
    if not inp_nome:
        st.stop()
    df = frequencia_nome(inp_nome)
    st.dataframe(df)
    #print(frequencia_nome(inp_nome))

if __name__ == "__main__":
    main()