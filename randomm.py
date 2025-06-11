import random

# print('Gerar 5 numeros aleatorio entre 1 e 50: \n')
# for i in range(5):
#     n = random.randint(1,50)
#     print(f'Numero Gerado: {n}')

# gerar numeros aleatorios float
# valor = random.random()
# print(f'Numero Gerado: {round(valor * 10,2)}')

# valor = random.uniform(1,100)
# print(f'Numero:{round(valor,2)}')


L = [2,4,6,9,10,13,25,45,23,56,78,67]

# n = random.choice(L)
# print(f'Numero escolhido:{n}')

# n = random.sample(L,3)
# print(f'Numeros escolhidos{n}')

# embaralhar

print(f"Exibir a lista original{L}")
print(f'Embaralhar a lista e exibi-la')
n = random.shuffle(L)
print(L)

