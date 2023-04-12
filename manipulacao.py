import pandas as pd 

data = {'nome': ['Alice', 'Bob', 'Charlie', 'Dave', 'Emily', 'Sebastiao', 'Elisson', 'Kayo', 'Maicon', 'Patricia'],
        'idade': [25, 30, 35, 40, 45, 30, 28, 35, 30, 28],
        'cidade': ['Rio de Janeiro', 'São Paulo', 'Belo Horizonte', 'Salvador', 'Recife', 'Lajedo', 'Bonito', 'Tuparetama', 'Gravatá', 'Garanhuns']}
df = pd.DataFrame(data)

''' 
 Exibe os 4 primeiros da lista
 print(df.head())

 Exibe os 8 primeiros da lista
 print(df.head(8))

 gera um resumo estatístico
 print(df.describe())

 Mostra as colunas apresentadas
 print(df.columns)

 Mostra quantas linhas e colunas
 print(df.shape)

 Ele vai retornar uma linha aleatoria para você
 print(df.sample())
 
 Abaixo será mostrado pessoas que tem 30 anos ou mais
 filtro = df['idade'] > 30 
 df_filtrado = df[filtro]
 print(df_filtrado)
 
 Será apresentado do maior para o menor em questão de idade
 df_ordenado = df.sort_values('idade', ascending=False)
 print(df_ordenado)
 
 Calcula a média de idade de cada estado
 df_agrupado = df.groupby('cidade').mean()
 df_agrupado
 ''' 

