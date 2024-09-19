import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('exports/preprocessed_data/preprocessed_data_dezembro.csv')

# Abrir o arquivo TXT para escrita
with open('exports/converted_data/data_dezembro.txt', 'w') as f:
    # Iterar sobre cada linha do DataFrame
    for _, row in df.iterrows():
        # Obter o texto da coluna 'text'
        texto = row['text']
        # Substituir qualquer caractere especial por espaço (se necessário)
        texto_limpo = texto.replace(',', '').replace('.', '')
        # Escrever as palavras separadas por espaço
        f.write(texto_limpo + '\n')
