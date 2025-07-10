import pandas as pd
df_ex = pd.DataFrame({
    'Produto':['Banana', 'Maça', None, 'Pera'],
    'Preço': [2.5, 3.0, 2.8, None],
    'Estoque': [100, None, 50, 70]
})
#Indentifique os valores nulos
print(df_ex.isnull())


#Preencha os valores de 'preço' com a média
df_ex['Preço'].fillna(df_ex['Preço'].mean(),inplace= True)


# Preencha os valores de 'estoque' com o valor anterior
df_fill_valor = df_ex.fillna(0)


# Remova linhas com 'Produto' ausente.
df_sem_nulos = df_ex.dropna()
print(df_sem_nulos)