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
# df_preco_tipo = dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')
# df_preco_tipo.plot(kind='barh', figsize=(14, 10), color='purple')
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
# analise_residencial = imoveis_residenciais.groupby(
#     'Tipo')[['Valor']].mean().sort_values('Valor')
# analise_residencial.plot(kind='barh', figsize=(14, 10), color="blue")

# %%
imoveis_residenciais.value_counts('Tipo')
# %%
apartamentos = imoveis_residenciais.query('Tipo == "Apartamento"')
apartamentos

# %%
# aplicando 0 como padrão em casos que estejam como na
dados = dados.fillna(0)
# %%
# verificando quantos valores nulos/na tem as nossas as colunas do nosso df
dados.isnull().sum()

# %%
# removendo os registros que possuem valor de alguel igual a zero
# pegando todos os indices dessa query
registros_a_remover = dados.query('Valor == 0 | Condominio == 0').index

# %%
dados.drop(registros_a_remover, axis=0, inplace=True)

# %%
# dados que possuam 1 quarto e aluguel menor que 1200
selecao1 = dados['Quartos'] == 1
dados[selecao1]
selecao2 = dados['Valor'] < 1200
dados[selecao2]
# %%


# %%
selecao_final = (selecao1) & (selecao2)
dados[selecao_final]
# %%
selecao = (dados['Quartos'] >= 2) & (
    dados['Valor'] < 3000) & (dados['Area'] > 70)
dados[selecao]
# %%
dados.to_csv('dados_apartamento', index=False)
# %%
pd.read_csv('../conhecendo_pandas/dados_apartamento.csv', delimiter=',')
# %%
dados['valor_por_mes'] = dados['Valor'] + dados['Condominio']

# %%
