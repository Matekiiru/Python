def mensagem():
    print('Olá a todos')


# mensagem()


def soma(a,b):

    print(a+b)

# soma(12,7)

def mult(x,y):
    return x * y

# a = 5
# b = 8

# c = mult(a,b)
# print(f'Produto de {a} e {b} é {c}')

def div(k, j):
    if j != 0:
     return k / j
    else:
       return 'Impossivel divider por zero!' 

# if __name__ == '__main__':
#     a = int(input('Digite um numero: '))
#     b = int(input('Digite outro numero: '))

#     r = div(a,b)
#     print(f'{a} dividido por {b} é igual a {r}')

# def quadrado(val):
#     quadrados = []
#     for x in val:
#         quadrados.append(x ** 2)
#     return quadrados

def contar(num=11, caractere='+'):
   for i in range(1, num):
      print(caractere)

if __name__ == '__main__':
    
    contar(6,'*')
  