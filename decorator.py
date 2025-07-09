def decorator_ex(funcao):
    def wrapper():
        print('Olá!')
        funcao()
        print('Prazer em conhecer!')
    return wrapper

@decorator_ex
def saudacao():
    print('Seja muito bem-vindo!')

saudacao()