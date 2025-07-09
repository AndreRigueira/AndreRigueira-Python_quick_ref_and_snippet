import requests
from datetime import datetime


def cotacao_dolar():
    link = 'https://economia.awesomeapi.com.br/last/USD-BRL'
    requisicao = requests.get(link)
    requisicao = requisicao.json()

    data = datetime.today().strftime('%d/%m/%Y')
    hora = datetime.now().strftime('%H:%M:%S')

    print(f'Cotação do Dolar em {data}, às {hora}')
    print(f'1 USD = R$ {float(requisicao['USDBRL']['bid']):.3f}')

cotacao_dolar()