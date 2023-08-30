import pandas as pd

# Carregando dataset corretamente que nesse caso usa o separador em ';'
data = pd.read_csv(r'C:\Users\olive\OneDrive\Área de Trabalho\Projeto github\raspagem\CusoPandas\GasPricesinBrazil_2004-2019.csv', sep=';')

# Exibe as 5 primeiras linha se deixar o () vasio
print(data.head())
print(60*'*')
# Exibe as informações do dataset ou tabela
print(data.info())
print(60*'*')
# Atributo 'shape'
print(f'O data frame possiu {data.shape[0]} linhas/observações/registros e {data.shape[1]} colunas/atributos/variáveis')
print(60*'*')


personagens_df = pd.DataFrame({
    'Nome': ['Luke Skywalker', 'yoda', 'Palpatine'],
    'Idade': [16, 1000, 70],
    'Peso': [70.5, 15.2, 60.1],
    'Eh jedi': [True, True, False]
})

print(personagens_df)
print(60*'*')
print(personagens_df.info())
print(60*'*')
# O atributo DataFrame.coluns retorna uma 'Lista" com os nomes de todas as colunas do data frame
print(personagens_df.columns)
print(60*'*')
# O atributo list modifica a apresentação das colunas igual uma lista 
print(list(personagens_df.columns))
print(60*'*')
# Para renomear colunas do data frame, utilize o metodo DataFram.rename, que retorna uma copia do data fram com as colunas renomeadas
personagem_renomeado = personagens_df.rename(columns={
    'Nome': 'Nome Completo', # Renomeia a coluna nome para Nome Completo
    'Idade': 'IDade'
})
print(personagem_renomeado)
print(60*'*')
# Para alterar a propria tabela pode passar o parâmetro 'inplace=Treu'
personagens_df.rename(columns={
    'Nome': 'Nome Completo', # Renomeia a coluna nome para Nome Completo
    'Idade': 'IDade'
}, inplace=True)
print(personagens_df)
print(60*'*')

# Para renomear todas as colunas de um data frame(Tabela) /n
# é passar uma lisa com os novos nomes das colunas para o atributo DataFrame.columns
personagens_df.columns = ['NOME', 'IDADE', 'PESO', 'EH_JEDI']
print(personagens_df)