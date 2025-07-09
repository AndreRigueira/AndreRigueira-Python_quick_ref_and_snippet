import time
import requests

def calcular_tempo(funcao):
    def wrapper():
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()
        print(f'Duração: {tempo_final - tempo_inicial}')
    return wrapper

@calcular_tempo
def pegar_cotacao_dolar():
    link = 'https://economia.awesomeapi.com.br/last/USD-BRL'
    requisicao = requests.get(link)
    requisicao = requisicao.json()    
    print(f'1 USD = R$ {float(requisicao['USDBRL']['bid']):.3f}')

pegar_cotacao_dolar()