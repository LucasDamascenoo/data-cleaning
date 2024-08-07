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

