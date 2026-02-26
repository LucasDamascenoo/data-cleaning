
import pandas as pd
import numpy as np

schema = {
    'Quantity':'int64',
    'Price Per Unit': 'float',
    'Total Spent':'float',
}

def clean(df: pd.DataFrame) -> pd.DataFrame:

    # limpar nomes das colunas
    df.columns = df.columns.str.strip()
    # remover nulos
    df = df.dropna()
    # remover valores inválidos
    df = df[~df.isin(['UNKNOWN','ERROR']).any(axis=1)]
    # aplicar schema
    df = df.astype(schema)
    # converter data
    df['Transaction Date'] = pd.to_datetime(
        df['Transaction Date'],
        errors='coerce'
    )
    # ordenar
    df = df.sort_values('Transaction ID').reset_index(drop=True)

    return df



