from nltk.corpus import stopwords
from string import punctuation
import nltk
from nltk.corpus import brown
from pymystem3 import Mystem
from string import punctuation
punctuation+="'"+'«'+'»'
russian_stopwords = stopwords.words("russian")

from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


from sklearn import svm

from sklearn.utils.multiclass import unique_labels
from nltk.corpus import stopwords
from string import punctuation
import pickle


class Predictor:
    punctuation += "'" + '«' + '»'
    #path = "D:\\pycharm\\support_nlp_model\\polls\\"
    def __init__(self):
        with open("D:\\pycharm\\support_nlp_model\\polls\\" +"vectorizer.pk", "rb") as f:
            self.tfidf_vectorizer = pickle.load(f)
        with open("D:\\pycharm\\support_nlp_model\\polls\\"+"SVMr.pk", "rb") as f:
            self.clfr = pickle.load(f)

    def text_tokenize(self, text):
        words_stop = stopwords.words("russian")
        words_stop += stopwords.words('english')
        words_stop += ["день", 'добрый ', "просить", "необходимо", "г", "год", "the", 'просьба', "спасибо"]

        for k in text:
            if k in punctuation:
                text = text.replace(k, " ")

        tokens = text.split(' ')
        tokens = [token for token in tokens if token not in words_stop \
                  and not token.isdigit()
                  and len(token) > 1
                  ]
        while '' in tokens:
            tokens.remove('')
        return tokens  # [''.join(text) for text in tokens]

    encode = {'Запрос на обслуживание (настройка рабочего места, предоставление доступа, установка ПО)': 0,
              'Ошибка в работе информационной системы (некорректная работа)': 1,

              'Сбой в работе (не работает ПК, Интернет, почта, ПО, не работает ИС)': 2,
              'Закупка': 3,
              'Запрос на изменение/доработку ИС': 4}
    decode = {0: 'Запрос на обслуживание (настройка рабочего места, предоставление доступа, установка ПО)',
              1: 'Ошибка в работе информационной системы (некорректная работа)',

              2: 'Сбой в работе (не работает ПК, Интернет, почта, ПО, не работает ИС)',
              3: 'Закупка',
              4: 'Запрос на изменение/доработку ИС'}

    def predict(self, text):
        tokens = self.text_tokenize(text)
        tokens = [' '.join(text) for text in [tokens]]
        tokens = self.tfidf_vectorizer.transform(tokens)
        # return self.clfr.predict(self.tfidf_vectorizer.transform([' '.join(t) for t in ['text']] ))
        #return self.clfr.predict(tokens)[0]
        return self.decode.get(self.clfr.predict(tokens)[0])

