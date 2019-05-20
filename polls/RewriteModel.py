from nltk.corpus import stopwords
from string import punctuation
punctuation+="'"+'«'+'»'
import pandas as pd


class RewriteModel()


    def __init__:
        filepath = ''
        data = pd.read_csv(filepath)
        words_stop = stopwords.words("russian")
        words_stop+=stopwords.words('english')
        words_stop+=["день",'добрый ',"просить","необходимо","г","год","the",'просьба',"спасибо"]
        #rds_stop+=["день",'добрый ''эл,''почтовый','почта', 'документ', "просить","необходимо","г","год","the",'просьба',"спасибо"]
        #print(words_stop)
        def text_tokenize(text):
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
            return tokens

        labels = {'Запрос на обслуживание (настройка рабочего места, предоставление доступа, установка ПО)': 0,
                  'Ошибка в работе информационной системы (некорректная работа)': 1,

                  'Сбой в работе (не работает ПК, Интернет, почта, ПО, не работает ИС)': 2,
                  'Закупка': 3,
                  'Запрос на изменение/доработку ИС': 4}

        data = data[(data['ЗаявкаВид']!='Проект (создание новой инфраструктуры, открытие нового офиса)')]
        data[(data['ЗаявкаВид']=='Консультация, обновление, запрос/изменение прав доступа')] = 'Ошибка в работе информационной системы (некорректная работа)'
        data = data.drop_duplicates('ЗаявкаОписание')
        data['text_format'] = data['ЗаявкаВид'].apply(text_tokenize)
        data['veiw_id'] = data['ЗаявкаКатегория'].factorize()[0]
        data['category_id'] = data['ЗаявкаВид'].copy()
        data['category_id'] = data['category_id'].apply(labels.get)

    #def train(self):

