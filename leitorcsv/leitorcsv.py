import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

print("\n\nIMPORTA DADOS DE UM CSV PARA O BANCO DE DADOS!!!\n")

# Cria o dataframe apartir do csv
dataframe = pd.read_csv(input('Caminho absoluto/relativo do CSV: '), sep=',', encoding='utf-8')
banco = input("Nome do bando de dados: ")

# Formata a data_inicio e a data_final, substituindo as "/" por "-"
dataframe['data_inicio'] = dataframe['data_inicio'].str.replace('/', '-')
dataframe['data_final'] = dataframe['data_final'].astype(str).str.replace('/', '-')

# Formata as datas em YYYY-MM-DD
dataframe['data_inicio'] = pd.to_datetime(dataframe['data_inicio'], dayfirst=True).dt.strftime('%Y-%m-%d')
dataframe['data_final'] = pd.to_datetime(dataframe['data_final'], dayfirst=True).dt.strftime('%Y-%m-%d')

#Conecta com o banco de dados e inserre os dados no mesmo
engine = create_engine(f'mysql+pymysql://root:@localhost/{banco}')

print("\nAdiconando os dados no banco de dados...")
try:
    dataframe.to_sql('expulsoes', con=engine, if_exists='append', index=False)
    print("\n-------------------------\nInserção bem-sucedida!!!\n-------------------------\n")
except SQLAlchemyError as e:
    print(f"Erro ao inserir os dados no banco de dados: {str(e)}")
