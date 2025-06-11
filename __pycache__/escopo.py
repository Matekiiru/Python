

var_global = "Ola Mundo!!"

def escreve_texto():
    global var_global
    var_global = "Bancos de Dados com SQL"
    var_local = "Jorge Amado"
    print(f'Variavel Global: {var_global}')
    print(f'Variavel local: {var_local}')


if __name__ == '__main__':
    print(f'Executar a funçao escreve texto:')
    escreve_texto()
    print(f'Tentar acessar a variavel global diretamente: {var_global}')
