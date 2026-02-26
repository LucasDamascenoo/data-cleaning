
import pandas as pd
from pathlib import Path
from src.config.config import PROCESSED_DIR
import os



DATA_DIR = Path(__file__).resolve().parent / 'data'

def load_clean_data(df,file_name):
    
    output_path = PROCESSED_DIR/ file_name
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    
    df.to_parquet(
        output_path,
        index=False
    )
    
    return output_path

