# %%
import pandas as pd

# %%
# importando os dados
data = pd.read_csv(
    "./students_Exam_Scores/data/Original_data_with_more_rows.csv")

# %%
data.head(1)
# %%
# DROPANDO COLUNAS

drop_columns = ['Unnamed: 0', 'EthnicGroup', 'LunchType']
data = data.drop(columns=drop_columns)
# %%
data.head()
# %%
# Renomeando as colunas
data.rename(columns={"ParentEduc": "Formação_dos_Pais",
            "TestPrep": "Preparação_do_teste"}, inplace=True)
data.head()


# %%
# DELETANDO DUPLICATAS
data.duplicated().value_counts()  # verificando qtds registros duplicatos temos
data.drop_duplicates(inplace=True)

# resentando o indice para que seja de acordo com a qtd de registros
data.reset_index().drop(columns="index")

# %%
# REMOVENDO VALORES NULOS
data["Gender"].isna().sum()  # verifica se existe valores nulos no dataset
# no nosso dataset não tem dados nulos, mas caso houvesse iamos usar
data.dropna(inplace=True)


# %%
# Alterando valor de uma coluna indidualmente
# usando replace
replace_dic = {'female': 'F', 'male': 'M'}
data['Gender'] = data['Gender'].replace(replace_dic)
data

# %%
# Alterando valor de uma coluna indidualmente
# usando apply e lambda
# data["Gender"] = data["Gender"].apply(lambda x: 'F' if x == 'female' else 'M')
# data
# %%
# criando uma nova coluna com a soma das notas
data['Total Score'] = data['MathScore'] + \
    data['ReadingScore'] + data['WritingScore']
data['Sucess'] = data['Total Score'].apply(
    lambda x: 'Sucess' if x > 210 else 'fail')
data['Sucess'].value_counts()
data

# %%

# %%
# exportando o dataset limpo
caminho = "./students_Exam_Scores/data/data_clear.xlsx"
data.to_excel(caminho, index=False)
