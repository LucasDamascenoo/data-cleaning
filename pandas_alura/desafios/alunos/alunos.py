# %%
import pandas as pd

# %%
# 1 - Importe o arquivo alunos.csv e armazene seu conteúdo em um DataFrame Pandas.
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'
dados = pd.read_csv(url, sep=',')
dados
# %%
# 2 - Visualize as primeiras 7 linhas do DataFrame e as 5 últimas.
dados.head(7)  # 7 primeiras
dados.tail(5)  # 5 ultimas
# %%
# 3) Confira a quantidade de linhas e colunas desse DataFrame.
dados.shape  # (18, 4)

# %%
# 4 - Confira a quantidade de linhas e colunas desse DataFrame
dados.info()
