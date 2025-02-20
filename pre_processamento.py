import pandas as pd
import re
import string
import unicodedata
import nltk
from nltk.corpus import stopwords
from emot.emo_unicode import UNICODE_EMOJI

# Download de recursos do NLTK
nltk.download('stopwords')
stopwords_pt = set(stopwords.words('portuguese'))

# adicionando outras stopwords
minhas_stopwords = {"voce", "sim",
                    "puta", "fodase"
                    "porra", "sobre",
                    "caralho", "gpt",
                    "merda", "cara",
                    "bosta", "dia",
                    "nao", "tao",
                    "pra", "chatgpt",
                    "pro", "tudo",
                    "vai", "pode",
                    "bing", "machine",
                    "copilot", "learning",
                    "ter", "gemini",
                    "inteligencia",
                    "vou", "artificial",
                    "sei", "openai",
                    "ate", "rede",
                    "fazer", "neural",
                    "tava", "acho",
                    "ver", "ainda",
                    "aqui", "assim",
                    "sao", "nada",
                    "faz", "gente"}
stopwords_pt.update(minhas_stopwords)

def preprocess_text(text):
    # Remove menções (strings começando com @)
    text = re.sub(r'@[A-Za-z0-9_]+', '', text)

    # Remove links
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    
    # Remove hashtags (strings começando com #)
    text = re.sub(r'#[A-Za-z0-9_]+', '', text)
    
    # Remove emojis
    text = ''.join([char for char in text if char not in UNICODE_EMOJI])
    
    # Converte para minúsculas
    text = text.lower()
    
    # Remove acentos
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')
    
    # Remove pontuações
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    
    # Remove stopwords em português e palavras com 2 ou menos caracteres
    text = ' '.join([word for word in text.split() if word.lower() not in stopwords_pt and len(word) > 2])

    return text

# Carrega o DataFrame combinado
combined_df = pd.read_csv('exports/combined_data_dezembro.csv')

# Executa o pre processamento
combined_df['text'] = combined_df['text'].apply(preprocess_text)

# Remove duplicados com base na coluna 'url'
combined_df.drop_duplicates(subset=['url'], inplace=True)
combined_df.drop_duplicates(subset=['text'], inplace=True)

# Remove linhas com texto vazio
combined_df = combined_df[combined_df['text'] != '']

# Remove tweets com 2 ou menos palavras
combined_df = combined_df[combined_df['text'].apply(lambda x: len(x.split()) > 2)]

# Salva o DataFrame pré-processado em um novo arquivo CSV
combined_df.to_csv('exports/preprocessed_data/preprocessed_data_dezembro.csv', index=False)

# Exibe o DataFrame pré-processado
print("DataFrame pré-processado:")
print(combined_df)
