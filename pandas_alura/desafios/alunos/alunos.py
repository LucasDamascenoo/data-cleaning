# %%
import pandas as pd

# %%
# 1 - Importe o arquivo alunos.csv e armazene seu conteúdo em um DataFrame Pandas.
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'
url_apt = "https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv"
dados = pd.read_csv(url, sep=',')
dados_apt = pd.read_csv(url_apt, sep=';')

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

# %%
# 1.Calcular a média de quartos por apartamento;
apto = dados_apt.query('Tipo == "Apartamento"')
media_quartos = apto['Quartos'].mean()
media_quartos

# %%
# 2. Conferir quantos bairros únicos existem na nossa base de dados;
len(dados_apt['Bairro'].unique())
dados_apt['Bairro'].nunique()
# %%
# 3. Analisar quais bairros possuem a média de valor de aluguel mais elevadas
top_cinco_alugueis = dados_apt.groupby(['Bairro', 'Tipo'])[['Valor']].mean(
).sort_values('Valor', ascending=False).round(2).head(5)
top_cinco_alugueis
# %%
top_cinco_alugueis.plot(kind='barh', figsize=(14, 10), color="blue")
