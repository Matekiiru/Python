# Lista =  Sequencia de VALORES 

# Sintaxe  nome_lista = [Valores]

n1 = [4,6,7,8,9,0,10]
n2 = [3,4,5,1,2,4,5,2]
valores = n1 + n2
# valores[0] = 9
# print('Concatenaçao de listas',valores)

# print(valores[0:2])
# print(valores[-2:])
# print(len(valores))
# print(sorted(valores,reverse=True))
# print(sum(valores))
# print(min(valores))
# print(max(valores))

# valores.append(13)
# print(valores)
# valores.pop(3)
# print(valores)
# valores.insert(3,21)
# print(valores)
# print(13 in valores)

# planetas = ['Mercurio','Venus','Marte','Saturno','Urano','Netuno']
# for planeta in planetas:
#     print(planeta)


# Exercicio 
bebidas = []

for i in range(5):
    print(f'Digite uma bebibda favorita:')
    bebida = input()
    bebidas.append(bebida)
bebidas.sort()
print(f'\nBebidas escolhidas:')
for bebida in bebidas:
    print(bebida)

print(f'\nSaude!')

