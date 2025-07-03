# juntar duas listas, item a item

objetos = ['sol','céu','sangue','grama','berinjela','bola 8']
cores = ['amarelo', 'azul', 'vermelho', 'verde', 'roxo', 'preto']


for objeto, cor in zip(objetos,cores):
    print(objeto, cor)