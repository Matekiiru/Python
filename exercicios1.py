# exercico 1  exercicios feitos no google colab
v1 = input("Digite o primeiro numero: ")
v2 = input("Digite o segundo numero: ")

if v1 > v2:
  print("O primeiro valor é maior")
else:
  print("O segundo valor é maior")



# exercico 2

salario = float(input("Informe seu salario"))

if salario <= 280.00:
  reaj = salario*0.20
  print("Seu antigo salario era",salario,"Seu novo salario é ",salario + reaj, "com reajuste de 20% e aumento de",reaj)
if salario > 280.00 and salario <= 700.00:
    reaj = salario*0.15
    print("Seu antigo salario era",salario,"Seu novo salario é ",salario + reaj, "com reajuste de 15% e aumento de",reaj)
if  salario > 700.00 and salario <= 1500.00 and salario:
      reaj = salario*0.5
      print("Seu antigo salario era",salario,"Seu novo salario é ",salario + reaj, "com reajuste de 5% e aumento de",reaj)
else:
  reaj = salario*0.1
  print("Seu antigo salario era",salario,"Seu novo salario é ",salario)


# exercico 3

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = (n1 + n2 + n3 + n4)/4
if media  == 10.0:
  print("Aprovado com distinção")
elif media > 7.0 :
  print("Aprovado")
elif media < 7.0:
  print("Reprovado")

# exercico 4

ano = int(input("Digite o ano do seu nascimento: "))

idade = ano - 2024

if idade < 16:
  print("Você não pode votar")
else:
  print("Você pode votar")

# exercico 5

senha = 1234

senha_digitada = int(input("Digite a senha: "))

if senha_digitada == senha:
  print("Acesso permitido")
else:
  print("Acesso negado")


# exercico 6

lados = int(input("Digite o numero de lados do poligono: "))
cm= float(input("Digite a medida do lado do poligono: "))
if lados < 3:
  print("Não é um poligono")
if lados >5:
  print("Polígono não identificado")
if lados == 3:
  print("Triangulo")
  print("A area do triangulo é ",(cm**2)/2)
elif lados == 4:
  print("Quadrado")
  print("A area do quadrado é ",cm**2)
elif lados == 5:
  print("Pentagono")
  print("A area do pentagono é ",(cm**2)/2)

# exercico 7

v1 = input("Digite o primeiro numero: ")
v2 = input("Digite o segundo numero: ")
v3 = input("Digite o terceiro numero: ")

if v1 > v2 and v1 > v3:
  print("O primeiro valor é maior",v1)
elif v2 > v1 and v2 > v3:
  print("O segundo valor é maior",v2)
else:
  print("O terceiro valor é maior",v3)

# exercico 8

angulo1 = float(input("Digite o primeiro angulo do triangulo: "))
angulo2 = float(input("Digite o segundo angulo do triangulo: "))
angulo3 = float(input("Digite o terceiro angulo do triangulo: "))

if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
  print("Triangulo retangulo")
  if angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
    print("Triangulo obtusangulo")
  else:
    print("Triangulo acutangulo")

