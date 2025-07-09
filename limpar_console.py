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
    print("Console limpo!  Rodando a aplicação...\n")

print('olá mundo')