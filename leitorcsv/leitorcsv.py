import pandas as pd
from sqlalchemy import create_engine

# Cria o dataframe apartir do csv
dataframe = pd.read_csv('csv/expulsoes.csv', sep=',', encoding='utf-8')

# Formata a data_inicio e a data_final, substituindo as "/" por "-"
dataframe['data_inicio'] = dataframe['data_inicio'].str.replace('/', '-')
dataframe['data_final'] = dataframe['data_final'].astype(str).str.replace('/', '-')

# Formata as datas em YYYY-MM-DD
dataframe['data_inicio'] = pd.to_datetime(dataframe['data_inicio'])
dataframe['data_inicio'] = dataframe['data_inicio'].dt.strftime('%Y-%m-%d')
dataframe['data_final'] = pd.to_datetime(dataframe['data_final'])
dataframe['data_final'] = dataframe['data_final'].dt.strftime('%Y-%m-%d')

#Conecta com o banco de dados e inserre os dados no mesmo
engine = create_engine('mysql+pymysql://root:@localhost/leitorcsv')
dataframe.to_sql('expulsoes', con=engine, if_exists='append', index=False)