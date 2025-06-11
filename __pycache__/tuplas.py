# tuplas são imutaveis


halogenios = ('F','Cl','Br','I','At')
gases_nobres = ('He','Ne','Ar','Xe','Kr','Rn')
elementos = halogenios + gases_nobres
print(halogenios)
print(len(halogenios))
print(halogenios[3])
t1 = ( 5,5,5,6,7,8,7,8,9,7,6,5,4)
print(elementos)
print('Cl' in halogenios)
print('Fe' in halogenios)
print(sum(t1))



grupo17= list(halogenios)
grupo17[0] = 'H'
print(grupo17)

grupo1 = ['Li','Na','K','Rb','Cs','Fr']

alcalinos = tuple(grupo1)
print(alcalinos)


