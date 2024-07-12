# %%
import pandas as pd
import matplotlib
# %%

# %%
url = "https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv"
dados = pd.read_csv(url, delimiter=';')
dados.head()
# %%
# Analise exploratorio dos dados
# %%
# QUAL O VALOR MÉDIO DO ALUGUEL POR TIPO DE ALUGUEL# %%
dados['Valor'].mean()
# %%
# %%
df_preco_tipo = dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')
df_preco_tipo.plot(kind='barh', figsize=(14, 10), color='purple')
# %%

# %%

# %%
