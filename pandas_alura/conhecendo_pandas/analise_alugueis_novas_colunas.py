# %%
import pandas as pd
import matplotlib
# %%

# %%
url = "https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv"
dados = pd.read_csv(url, delimiter=';')


# %%
# criando colunas de valores
dados['Valor_por_mes'] = dados['Valor'] + dados['Condominio']
dados['Valor_por_ano'] = dados['Valor_por_mes'] * 12 + dados['IPTU']
# %%
dados['Possui_suite'] = dados['Suites'].apply(
    lambda x: "Sim" if x > 0 else "Não")
dados.head()

# %%
dados.to_csv('dados_completos.csv', index=False, sep=';')
