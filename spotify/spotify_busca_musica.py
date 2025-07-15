# pip install spotipy

import spotipy, os
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# --- SUAS CREDENCIAIS AQUI ---
load_dotenv()
# Cole seu Client ID e Client Secret aqui
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
# --- FIM DAS CREDENCIAIS ---

# Define as credenciais para o Spotipy
# Isso é como mostrar sua "identidade" para o Spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
                                                           client_secret=CLIENT_SECRET))

# A música que você quer buscar
nome_musica = "Bohemian Rhapsody"
nome_artista = "Queen"

# Realiza a busca no Spotify
# Estamos procurando por uma faixa (track) com o nome e artista que definimos
resultados = sp.search(q=f'track:{nome_musica} artist:{nome_artista}', type='track')

# Verifica se encontramos algum resultado
if resultados['tracks']['items']:
    # Pega a primeira música da lista de resultados
    primeira_musica = resultados['tracks']['items'][0]

    # Imprime as informações da música
    print(f"Nome da Música: {primeira_musica['name']}")
    print(f"Artista: {primeira_musica['artists'][0]['name']}")
    print(f"Álbum: {primeira_musica['album']['name']}")
    print(f"URL de Visualização: {primeira_musica['external_urls']['spotify']}")
else:
    print(f"Não foi possível encontrar a música '{nome_musica}' do artista '{nome_artista}'.")
