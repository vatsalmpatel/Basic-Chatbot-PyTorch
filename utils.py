import nltk
from nltk.stem.porter import PorterStemmer

def tokenize(sentence):
    nltk.download('punkt')
    return nltk.word_tokenize(sentence)

def stem(word):
    stemmer = PorterStemmer()
    return stemmer.stem(word.lower())

def bag_of_words(toeknized_sentence,all_words):
    pass