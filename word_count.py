import os
from collections import Counter

# Defina o diretório onde estão os arquivos de texto
directory = 'exports/converted_data'

# Função para ler e juntar todo o conteúdo dos arquivos
def read_and_combine_files(directory):
    all_text = ''
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):  # Verifica se o arquivo é um .txt
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                all_text += file.read() + ' '  # Junta o conteúdo e adiciona um espaço entre arquivos
    return all_text

# Função para contar as palavras
def count_words(text):
    words = text.split()  # Separa as palavras por espaços
    return Counter(words)

# Função principal
def main():
    combined_text = read_and_combine_files(directory)
    word_count = count_words(combined_text)

    # Filtra palavras com frequência maior que 4
    filtered_word_count = [(word, count) for word, count in word_count.items() if count > 4]

    # Defina o nome do arquivo de saída
    output_file = os.path.join(directory, 'resultado_palavras.txt')

    # Escreve os resultados no arquivo TXT separado por vírgulas
    with open(output_file, 'w', encoding='utf-8') as f:
        for word, count in filtered_word_count:
            f.write(f'{word},{count}\n')

    print(f'Resultado escrito no arquivo: {output_file}')

if __name__ == '__main__':
    main()
