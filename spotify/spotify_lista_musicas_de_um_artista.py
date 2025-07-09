import json
import os
import platform

def clear_console():
    """Limpa o console."""
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

# Exemplo de uso:
if __name__ == "__main__":
    clear_console()
    #print("Console limpo!  Rodando a aplicação...")
    
    # Define o nome do arquivo JSON que vamos ler
    nome_arquivo_json = './spotify/spotify.json'

    # Pergunta ao usuário qual artista ele quer buscar
    artista_desejado = input("Digite o nome do artista que você quer buscar: ")

    # Usamos um SET para guardar os nomes das músicas únicas encontradas
    # Um set automaticamente garante que cada item seja único
    musicas_unicas_do_artista = set()

    try:
        # Abre e lê o arquivo JSON
        with open(nome_arquivo_json, 'r', encoding='utf-8') as f:
            dados_playlists = json.load(f)

        print(f"\nBuscando músicas únicas de '{artista_desejado}' nas suas playlists...\n")

        # Itera sobre cada playlist nos dados carregados
        for playlist in dados_playlists:
            # Itera sobre cada música dentro da playlist atual
            for musica in playlist['musicas']:
                # Verifica se o nome do artista da música corresponde ao artista desejado
                if musica['artista'].lower() == artista_desejado.lower():
                    # Adiciona o nome da música ao SET
                    # Se a música já estiver no set, ela não será adicionada novamente
                    musicas_unicas_do_artista.add(musica['nome_musica'])

        # Exibe os resultados
        if musicas_unicas_do_artista:
            print(f"Você tem {len(musicas_unicas_do_artista)} música(s) única(s) de '{artista_desejado}' em suas playlists:")
            # Converte o set para uma lista para poder iterar e mostrar de forma ordenada (opcional)
            # e para numerar as músicas facilmente
            lista_musicas_ordenada = sorted(list(musicas_unicas_do_artista))
            for i, musica_nome in enumerate(lista_musicas_ordenada):
                print(f"  {i+1}. {musica_nome}")
        else:
            print(f"Nenhuma música de '{artista_desejado}' encontrada nas suas playlists.")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo_json}' não foi encontrado. Certifique-se de que ele está na mesma pasta do seu script Python.")
    except json.JSONDecodeError:
        print(f"Erro: Não foi possível ler o arquivo '{nome_arquivo_json}'. Verifique se ele é um JSON válido.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")