import requests
import threading
import datetime
import json
import random
import os 
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0",
] #Adicione mais User-Agents conforme sua necessidade

def obter_user_agent_aleatorio():
     return random.choice(user_agents)

def testar_caminho(url_alvo, caminho, resultados):
    url_teste = f"{url_alvo}/{caminho}"
    headers = {"User-Agent" : obter_user_agent_aleatorio()}

    try:
        resposta = requests.get(url_teste, headers=headers, timeout=5)

        if resposta.status_code in [200, 301, 403]:
             resultado = {
                  "url": url_teste,
                  "status_code": resposta.status_code,
                  "content_length":len(resposta.content)
             }
             resultados.append(resultado)
             print(f"{url_teste} - Status: {resposta.status_code} - Tamanho {len(resposta.content)}")
             
    except requests.RequestException:
         print(f"Falha ao acessar {url_teste}")



def salvar_resultados(url_alvo, resultados):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Criar pasta 'resultados' se não existir
    pasta_resultados = "resultados"
    if not os.path.exists(pasta_resultados):
        os.makedirs(pasta_resultados)

    nome_arquivo = f"{pasta_resultados}/resultados_fuzzer_{timestamp}.json"

    dados = {
        "target": url_alvo,
        "timestamp": timestamp,
        "found_paths": resultados
    }

    with open(nome_arquivo, "w") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    print(f"Resultados salvos em {nome_arquivo}")


def fuzzer(url_alvo, wordlist):
     
     resultados = []

     threads = []
     
     for caminho in wordlist:
        thread = threading.Thread(target=testar_caminho, args=(url_alvo, caminho, resultados))
        threads.append(thread)
        thread.start()

     for thread in threads:
         thread.join()

     salvar_resultados(url_alvo, resultados)
