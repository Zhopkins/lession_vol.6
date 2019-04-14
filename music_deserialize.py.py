# 2: Создать модуль music_deserialize.py.
# В этом модуле открыть файлы group.json и group.pickle,
# прочитать из них информацию. Получить объект — словарь из предыдущего задания.

import json
import pickle


with open('group.json') as yellowcard:
    myjsonobject = json.load(yellowcard) # юзаем load - загрузка объекта из файла json

print(myjsonobject)

# открываем файл для чтения байтов (rb)

with open('group.pickle', 'rb') as yellowcard:
    mypickleobject = pickle.load(yellowcard) # юзаем load - загрузка объекта из файла

print(mypickleobject)
