import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy
import string
from gensim.models import Word2Vec
from typing import List
from langdetect import detect


nltk.download('punkt')
nltk.download('stopwords')

def tokenizacion_texto(texto):
    stop_words = stopwords.words('english')
    texto = texto.lower()
    tokens = word_tokenize(texto)
    text_filtrado = [word for word in tokens if not word in stop_words]
    return text_filtrado

## Creacion de word embeding
def procesamiento_tokenizacion(oraciones):
    oraciones_limpias = []
    stop_words = stopwords.words('english')
    for oracion in oraciones:
        tokens = [word.lower() for word in oracion.translate(str.maketrans('', '', string.punctuation)).split() if word.lower() not in stop_words and word.isalpha()]
        english_words = [word for word in tokens if detect(word) == 'en']
        if len(english_words)>5 :
            oraciones_limpias.append(english_words)

    return oraciones_limpias

def procesamiento_tokenizacion_spacy(oraciones):
    oraciones_limpias = []
    stop_words = stopwords.words('english')

    tokens = [word.lower() for word in oraciones.translate(str.maketrans('', '', string.punctuation)).split() if
              word.lower() not in stop_words and word.isalpha()]
    english_words = [word for word in tokens if detect(word) == 'en']
    if len(english_words) > 5:
        oraciones_limpias.append(english_words)
    return oraciones_limpias
def word2vec_oraciones(expedientes_laborales_oraciones):
    model = Word2Vec(sentences=expedientes_laborales_oraciones,
                     vector_size=500, window =4, min_count=1, workers=8)
    return model
