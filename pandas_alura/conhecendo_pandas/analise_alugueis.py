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
dados['Tipo'].unique()
# %%
# Precisamos dividir os imoveis comerciais e residenciais da nossa analise

imoveis_comerciais = ['Conjunto Comercial/Sala', 'Prédio Inteiro', 'Loja/Salão', 'Galpão/Depósito/Armazém', 'Casa Comercial',
                      'Terreno Padrão', 'Loja Shopping/ Ct Comercial', 'Chácara', 'Loteamento/Condomínio', 'Sítio', 'Pousada/Chalé', 'Hotel', 'Indústria']
# %%
imoveis_residenciais = dados.query(
    '@imoveis_comerciais != Tipo')  # podemos usar o not in / in
# %%
analise_residencial = imoveis_residenciais.groupby(
    'Tipo')[['Valor']].mean().sort_values('Valor')
analise_residencial.plot(kind='barh', figsize=(14, 10), color="blue")

# %%
imoveis_residenciais.value_counts('Tipo')
# %%
apartamentos = imoveis_residenciais.query('Tipo == "Apartamento"')
apartamentos
