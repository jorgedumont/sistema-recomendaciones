import numpy as np
from nltk.corpus import stopwords

def convert_lower_case(data):
    return np.char.lower(data)

def removepunctuation(data):
    symbols = "!$%&()*+-./:;<=>?@[]^`{|}~\n\""
    for i in range(len(symbols)):
        data = np.char.replace(data, symbols[i], ' ')
        data = np.char.replace(data, "  ", " ")
    data = np.char.replace(data, ',', '')
    return data

def remove_apostrophe(data):
    return np.char.replace(data, "'", "")

def preprocess(data):
    data = convert_lower_case(data)
    data = removepunctuation(data) 
    data = remove_apostrophe(data)
    return data

def listaParada(data):
    stop_words = stopwords.words('spanish')
    new_text = ""
    for w in str(data).split():
        if w not in stop_words and len(w) > 1:
            new_text = new_text + " " + w
    return new_text    