import numpy as np
import nltk
# nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentence):
    """
    Divide la frase en un arrray de palabras/tokens
    un token puede ser una palabra o, un caracter numerico
    o uno de puntuacion.
    """
    return nltk.word_tokenize(sentence)


def stem(word):
    """
    stemming = Encuentra la raiz de la palabra
    Por ejmeplo:
    words = ["organize", "organizes", "organizing"]
    words = [stem(w) for w in words]
    -> ["organ", "organ", "organ"]
    """
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, words):
    """
    Devuelve una bolsa de arrays de con palabras:
    1 para cada palabra conocida que exista en la frase y 0
    para aquellas palabras que no existan
    Por ejemplo:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bog   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """
    # cada palabra
    sentence_words = [stem(word) for word in tokenized_sentence]
    # inicializa la bolsa con 0 para cada palabra
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag