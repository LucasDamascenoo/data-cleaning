#%%
import pandas as pd
import numpy as np
from pathlib import Path
from src.config.config import RAW_DIR



#funcao que ler o caminho e verifica se ele existe
def read_csv(file_name:str) -> pd.DataFrame:
    path = RAW_DIR /file_name
    
    if not path.exists():
        raise FileNotFoundError(f'arquivo nao encontrado: {path}')
    
    return pd.read_csv(path)

    