chave = input("Digite a chave: ")
mensagem = input("Digite a sua frase: ")

# repora o k pelo h e tirar os espaços da string
chave = chave.upper().replace("K", "H")
mensagem = mensagem.upper().replace("K", "H").replace(" ", "")

# verfificar e tirar as palavras duplicadas
chavef = ""
for char in chave:
    if char not in chavef:
        chavef += char

#coloca as letras restantes do alfabeto verificando quais faltam
alfabeto = "ABCDEFGHIJLMNOPQRSTUVWXYZ"
for char in alfabeto:
    if char not in chavef:
        chavef += char

# cria os pares de letras e aplica as regras da codificaçao
pares = []
i = 0
while i < len(mensagem):
    if i + 1 < len(mensagem) and mensagem[i] == mensagem[i + 1]:
        # coloca o x se for repetido
        pares.append(mensagem[i] + 'X')
        i += 1
    else:
        if i + 1 < len(mensagem):
            pares.append(mensagem[i] + mensagem[i + 1])
            i += 2
        else:
          # se for so uma letra coloca o x tbm
            pares.append(mensagem[i] + 'X')
            i += 1

# encriptaçao né
cifrado = []

for par in pares:
    letra1, letra2 = par

    #coordenadas
    index1 = chavef.index(letra1)
    index2 = chavef.index(letra2)

# calcula as coordenadas com o modulo
    li1, c1 = index1 // 5, index1 % 5
    li2, c2 = index2 // 5, index2 % 5

# regras da cifra, se ta uma do lado da outra etc...
    if li1 == li2:
        cifrado.append(chavef[li1 * 5 + (c1 + 1) % 5])
        cifrado.append(chavef[li2 * 5 + (c2 + 1) % 5])
    elif c1 == c2:
        cifrado.append(chavef[((li1 + 1) % 5) * 5 + c1])
        cifrado.append(chavef[((li2 + 1) % 5) * 5 + c2])
    else:
        cifrado.append(chavef[li1 * 5 + c2])
        cifrado.append(chavef[li2 * 5 + c1])

print(f"Mensagem criptografada: {''.join(cifrado)}")