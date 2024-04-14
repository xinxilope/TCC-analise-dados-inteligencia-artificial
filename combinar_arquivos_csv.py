import os
import pandas as pd

def merge_csv_files(folder_path):
    # Lista todos os arquivos na pasta
    file_list = os.listdir(folder_path)
    
    # Filtra apenas os arquivos CSV
    csv_files = [file for file in file_list if file.endswith('.csv')]
    
    # Verifica se há pelo menos um arquivo CSV na pasta
    if not csv_files:
        print("Não há arquivos CSV na pasta.")
        return None
    
    # Inicializa um DataFrame vazio para armazenar os dados combinados
    combined_df = pd.DataFrame()
    
    # Itera sobre os arquivos CSV e os combina em um DataFrame único
    for file in csv_files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        combined_df = pd.concat([combined_df, df], ignore_index=True)
    
    return combined_df

# Pasta contendo os arquivos CSV
folder_path = 'exports'

# Chama a função para combinar os arquivos CSV
merged_df = merge_csv_files(folder_path)

# Se o DataFrame combinado não estiver vazio, faça o que desejar com ele
if merged_df is not None:
    print("DataFrame combinado:")
    print(merged_df)
    # Você pode salvar o DataFrame combinado em um novo arquivo CSV, se desejar
    merged_df.to_csv('combined_data/combined_data.csv', index=False)
