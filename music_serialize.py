# Создать модуль music_serialize.py.
# В этом модуле определить словарь для вашей любимой музыкальной группы, например:
# my_favourite_group = {
# ‘name’: ‘Г.М.О.’,
# ‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
# ‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
# {‘name’: ‘Шапито’,‘year’: 2014}]}
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты,
# вывести результаты в терминал. Записать результаты в файлы group.json,
# group.pickle соответственно. В файле group.json указать кодировку utf-8.

import json
import pickle



my_favourite_group = {
    'name': 'Yellowcard',
    'tracks': ['Only One', 'Dear Bobbie'],
    'Albums': [{'name': 'Ocean Avenue', 'year': 2003},
               {'name': 'Lights and Sounds', 'year': 2006}]
}

#открываем на запись файл (создаем, т.к. его нет и стоит w), третьим параметром передаем кодировку utf-8
with open('group.json', 'w', encoding='utf-8') as yellocard:
    json.dump(my_favourite_group, yellocard) #юзаем dump - сохранение объекта в файл в формате json

terminaljson = json.dumps(my_favourite_group)
print(terminaljson)


with open('group.pickle', 'wb') as yellocard2: # открываем файл на запись в байтах
    pickle.dump(my_favourite_group, yellocard2) #юзаем dump - сохранение объекта в файл

terminalpickle = pickle.dumps(my_favourite_group)
print(terminalpickle)
