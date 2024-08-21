import requests

auth_token = "dc07c71f7c2950a3fc58ec6c64a45bc14f26af77d180e136cb1d29d261778192"

def connect_to_api(key):
    request = request.get(f"https://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token={key}").text

    if request != "true":
        raise Exception("ERRO AO AUTENTICAR A API!")

    


def get_linha_info(auth, termo):
    headers = {
        "Authorization": f"{auth}"  # Adiciona "Bearer" antes do token
    }
    request_url = f"https://api.olhovivo.sptrans.com.br/v2.1/Linha/Buscar?termosBusca={termo}"
    
    try:
        resposta = requests.get(request_url, headers=headers)
        resposta.raise_for_status()  # Lança um erro para códigos de status HTTP 4xx/5xx
        
        # Tenta converter a resposta para JSON
        data = resposta.json()
        
        # Retorna a resposta JSON para fácil manipulação
        return data
    except requests.exceptions.HTTPError as err:
        print(f"RESPOSTA: {resposta.text}")
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
    except ValueError as err:
        print(f"Error decoding JSON: {err}")

# Testa a função
linha_info = get_linha_info(auth_token, "8000")
print(linha_info)


connect_to_api(auth_token)