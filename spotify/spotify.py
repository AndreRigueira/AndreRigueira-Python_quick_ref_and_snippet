import spotipy, os
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# --- SUAS CREDENCIAIS E REDIRECT URI AQUI ---
load_dotenv()
# Cole seu Client ID e Client Secret aqui
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
# O URI de redirecionamento que você configurou no painel de desenvolvedores do Spotify
REDIRECT_URI = 'http://127.0.0.1:8888/callback' # Ou http://localhost/
# --- FIM DAS CREDENCIAIS ---

# Define as "permissões" (scopes) que sua aplicação precisa
# 'playlist-read-private': Para ler suas playlists privadas
# 'playlist-read-collaborative': Para ler playlists colaborativas
SCOPE = "playlist-read-private playlist-read-collaborative"

# Cria a instância de autenticação do Spotify
# Isso vai cuidar do processo de pedir sua permissão
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

# 1. Pegar as playlists do usuário logado
print("Buscando suas playlists...")
# O método 'current_user_playlists()' pega as playlists do usuário autenticado
playlists = sp.current_user_playlists()

# 2. Iterar sobre cada playlist e mostrar suas músicas
if playlists['items']:
    for i, playlist in enumerate(playlists['items']):
        print(f"\n--- Playlist {i+1}: {playlist['name']} ---")
        print(f"Número de músicas: {playlist['tracks']['total']}")

        # Pega os detalhes das músicas da playlist
        # Precisamos de um loop porque playlists grandes podem ter muitas músicas
        # e o Spotify envia em "páginas" de 100 músicas por vez
        results = sp.playlist_items(playlist['id'])
        tracks = results['items']
        while results['next']: # Se houver mais músicas para buscar (próxima página)
            results = sp.next(results)
            tracks.extend(results['items'])

        # Mostra o nome de cada música
        if tracks:
            for j, item in enumerate(tracks):
                track = item['track']
                if track: # Verifica se a faixa não é nula (às vezes pode acontecer)
                    print(f"  {j+1}. {track['name']} - {track['artists'][0]['name']}")
                else:
                    print(f"  {j+1}. [Música indisponível]")
        else:
            print("  Esta playlist não tem músicas.")
else:
    print("Você não tem nenhuma playlist (ou não foi possível encontrá-las).")