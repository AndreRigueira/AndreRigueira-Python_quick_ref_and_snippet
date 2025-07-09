import json

# Define o nome do arquivo JSON que vamos ler
nome_arquivo_json = './spotify/spotify.json'

# O artista que você quer buscar
# artista_desejado = "Queen" # Você pode mudar para qualquer artista!
print('♫ Busca de Músicas por Artista nas minhas Playlists ♫')
artista_desejado = input('Digite o nome do Artista/Banda: ')

# Lista para guardar as músicas encontradas
musicas_do_artista = []

try:
    # Abre e lê o arquivo JSON
    # 'r' significa modo de leitura
    with open(nome_arquivo_json, 'r', encoding='utf-8') as f:
        # Carrega o conteúdo do JSON para uma estrutura de dados Python (lista de dicionários)
        dados_playlists = json.load(f)

    print(f"Buscando músicas de '{artista_desejado}' nas suas playlists...\n")

    # Itera sobre cada playlist nos dados carregados
    for playlist in dados_playlists:
        nome_playlist = playlist['nome_playlist']
        # Itera sobre cada música dentro da playlist atual
        for musica in playlist['musicas']:
            # Verifica se o nome do artista da música corresponde ao artista desejado
            # Usamos .lower() para comparar sem se importar com maiúsculas/minúsculas
            if musica['artista'].lower() == artista_desejado.lower():
                # Se encontrou, adiciona à nossa lista de resultados
                musicas_do_artista.append({
                    "nome_musica": musica['nome_musica'],
                    "album": musica['album'],
                    "playlist": nome_playlist
                })

    # Exibe os resultados
    if musicas_do_artista:
        print(f"Músicas de '{artista_desejado}' encontradas nas suas playlists:")
        for i, musica_encontrada in enumerate(musicas_do_artista):
            print(f"  {i+1}. '{musica_encontrada['nome_musica']}' (Álbum: '{musica_encontrada['album']}') na playlist: '{musica_encontrada['playlist']}'")
    else:
        print(f"Nenhuma música de '{artista_desejado}' encontrada nas suas playlists.")

except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo_json}' não foi encontrado. Certifique-se de que ele está na mesma pasta do seu script Python.")
except json.JSONDecodeError:
    print(f"Erro: Não foi possível ler o arquivo '{nome_arquivo_json}'. Verifique se ele é um JSON válido.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")