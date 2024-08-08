# Pandas I/O (Input e Output)

Nesse curso vamos aprender a ler e gravar dados em diversas fontes diferentes.


## Lendo Csv

```python:

dados = pd.read_csv('./data/superstore_data.csv', sep=',')

```

- sep : é parametro que vai setar o separador do arquivo csv (por padrão é ,)

- nrows : define quantas x linhas vamos ler na chamada no csv

- usecols: podemos escolher quais colunas vamos ler na chamada do csv ['id','income']

- skiprows: podemos definir quantas linhas queremos ignorar skiprows=3

## Escrevendo csv

```python:

dados.to_csv('clientes_mercado.csv',index=False)

```

- Index: define se vamos criar ou não uma nova coluna de index (normalmente colocamos False)

## Lendo Planilhas

```python:

dados = pd.read_excel('./data/superstore_data.xlsx', sheet_name='emissao',usecols='A:D')

```

- sheet_name: seleciona uma determinada aba do excel
- usecols: podemos escolher quais colunas vamos ler na chamada do excel ['id','income']
- nrows : define quantas x linhas vamos ler na chamada no excel

## Escrevendo Planilhas

```python:

dados.to_excel('c02_percapita.xlsx',index=False)

```

- Index: define se vamos criar ou não uma nova coluna de index (normalmente colocamos False)


## Lendo Jsons

 - Json são bastante usados em Apis

 - Podemos criar normalize : A função json_normalize() é capaz de converter cada registro da lista em uma linha de forma tabular.



```python:

dados = pd.read_json('./data/emissoes_CO2.json')
dados_normalizados = pd.json_normalize(dados['Paciente'])

```

## Escrevendo Json

```python:

df_json.to_json('arquivo_sem_indice.json', index = False, orient = 'split')

```


## Lendo tabelas (sql)

- para utilizar bandos de dados no pandas, precisando importar o sqlalchemy

- dependendo do banco de dados precisamos ter drivers especificos

```python:

query = """
SELECT id, nome, salario
FROM empregados
WHERE departamento = 'Vendas'
"""
df = pd.read_sql_query(query, con=engine)

```

```python:

nome_da_tabela = 'nome_da_tabela'

# Carregar a tabela inteira em um DataFrame
df = pd.read_sql_table(nome_da_tabela, con=engine)

```