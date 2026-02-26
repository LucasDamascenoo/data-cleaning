
from src.io.reader import read_csv
from src.cleaning.cleaner import clean
from src.io.write import load_clean_data

import logging

#Configuracao do Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)



def run_process():
    df = read_csv('sales.csv')
    df_clean = clean(df)
    
    load_clean_data(df_clean,'sales_clean.parquet')
    
    logging.info(f'processo completado, dado limpo e  salvo ')
    
    
    

if __name__ == "__main__":
    run_process()