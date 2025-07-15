import spotipy, os
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import json # Importamos a biblioteca json

# --- SUAS CREDENCIAIS E REDIRECT URI AQUI ---
load_dotenv()
# Cole seu Client ID e Client Secret aqui
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
# O URI de redirecionamento que você configurou no painel de desenvolvedores do Spotify
REDIRECT_URI = 'http://127.0.0.1:8888/callback'
# --- FIM DAS CREDENCIAIS ---

SCOPE = "playlist-read-private playlist-read-collaborative"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

print("Buscando suas playlists e músicas para salvar em JSON...")

# Lista que vai guardar todas as informações que queremos salvar
# Cada item desta lista será um dicionário representando uma playlist
todas_as_playlists_dados = []

playlists = sp.current_user_playlists()

if playlists['items']:
    for i, playlist in enumerate(playlists['items']):
        playlist_data = {
            "nome_playlist": playlist['name'],
            "id_playlist": playlist['id'],
            "total_musicas": playlist['tracks']['total'],
            "musicas": [] # Lista para guardar os detalhes de cada música
        }

        print(f"Processando playlist: {playlist['name']}")

        results = sp.playlist_items(playlist['id'])
        tracks = results['items']
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])

        if tracks:
            for j, item in enumerate(tracks):
                track = item['track']
                if track:
                    # Adiciona os detalhes da música à lista de músicas da playlist
                    playlist_data["musicas"].append({
                        "nome_musica": track['name'],
                        "artista": track['artists'][0]['name'],
                        "album": track['album']['name'],
                        "id_musica": track['id']
                    })
        else:
            print(f"  Playlist '{playlist['name']}' não tem músicas ou estão indisponíveis.")

        # Adiciona os dados completos desta playlist à lista geral
        todas_as_playlists_dados.append(playlist_data)
else:
    print("Você não tem nenhuma playlist (ou não foi possível encontrá-las).")

# --- Salvando os dados no arquivo JSON ---
nome_arquivo_json = 'spotify.json'
try:
    with open(nome_arquivo_json, 'w', encoding='utf-8') as f:
        # Usamos json.dump para escrever a estrutura de dados Python no arquivo JSON
        # indent=4 serve para formatar o JSON de forma mais legível (com recuo)
        # ensure_ascii=False permite que caracteres especiais (acentos, etc.) sejam salvos corretamente
        json.dump(todas_as_playlists_dados, f, indent=4, ensure_ascii=False)
    print(f"\nDados salvos com sucesso em '{nome_arquivo_json}'!")
except IOError as e:
    print(f"Erro ao salvar o arquivo '{nome_arquivo_json}': {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
