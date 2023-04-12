import pandas as pd
import pandas_profiling

arquivo = 'acidentes2021.csv'
dataset = pd.read_csv(arquivo, sep=';', header=0)
print('Base carregada com sucesso')

'''
Exibe as 5 primeiras linhas
print(dataset.head())

Exibe dados da coluna moto e auto
dataset2 = dataset[["moto", "auto"]]
print(dataset2.info())

Apresenta quantas colona tem vazias em cada categoria
print('Numero de colona vazias NaN')
print(dataset.isna().sum())

Removendo colunas indesejadas
colunas_indesejadas = ['numero', 'detalhe_endereco_acidente', 'complemento', 
                       'num_semaforo', 'acidente_verificado', 'situacao_semaforo', 'divisao_via1', 'divisao_via2', 'divisao_via3']
print(f'Removendo as colunas indesejadas: {colunas_indesejadas}')
print(f'Dataset antes da remoção das colunas: {dataset.shape[0]} linhas e {dataset.shape[1]} colunas')

dataset_novo = dataset.drop(labels=colunas_indesejadas, axis=1)

print(f'Dataset após a remoção das colunas: {dataset_novo.shape[0]} linhas e {dataset_novo.shape[1]} colunas\n')
print(dataset_novo.head())

Mostra a situação das ocorrência
print(dataset_novo['situacao'].unique())

Status das ocorrencias
print('TOTAL DE SITUAÇÕES FINALIZADAS --->',
(dataset_novo['situacao']=="FINALIZADA").sum())
print('TOTAL DE SITUAÇÕES CANCELADAS --->',
(dataset_novo['situacao']=="CANCELADA").sum())
print('TOTAL DE SITUAÇÕES DUPLICIDADE --->',
(dataset_novo['situacao']=="DUPLICIDADE").sum())
print('TOTAL DE SITUAÇÕES EVADIU-SE --->',
(dataset_novo['situacao']=="EVADIU-SE").sum())

Transformando as categorias em valores números
dataset_novo.loc[dataset_novo['situacao'] == 'FINALIZADA', 'situacao'] = 0
dataset_novo.loc[dataset_novo['situacao'] == 'CANCELADA', 'situacao'] = 1
dataset_novo.loc[dataset_novo['situacao'] == 'DUPLICIDADE', 'situacao'] = 2
dataset_novo.loc[dataset_novo['situacao'] == 'EVADIU-SE', 'situacao'] = 3

Usando os valores númericos 
print('TOTAL DE SITUAÇÕES FINALIZADAS --->',
(dataset_novo['situacao']==0).sum())
print('TOTAL DE SITUAÇÕES CANCELADAS --->',
(dataset_novo['situacao']==1).sum())
print('TOTAL DE SITUAÇÕES DUPLICIDADE --->',
(dataset_novo['situacao']==2).sum())
print('TOTAL DE SITUAÇÕES EVADIU-SE --->',
(dataset_novo['situacao']==3).sum())

Transformando a analise de dados / manipulação em grafico
profile = pandas_profiling.ProfileReport(dataset_novo)
print(profile)


Transformando o grafico em arquivo HTML
profile.to_file("acidentes.html")


'''

