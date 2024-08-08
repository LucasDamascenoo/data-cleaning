# %%
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, inspect
# %%
sqlalchemy.__version__
# %%
dados = pd.read_json('./data/emissoes_CO2.json')
dados_normalizados = pd.json_normalize(dados['Paciente'])
dados

# %%
