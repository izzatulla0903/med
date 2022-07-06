# javaScript object Nitation - json
# единный формат хранения и передачи данных медлу 
# компьютерами сервисами приложениями и языками программирования через сеть интернет
# <filename>.json


# {
#     "id": 1,
#     "autor": "jhon",
#     "posts": []
# } - это JSON задача научиться переводить JSON в пайтон dict



#!!!!LS object == {}
#PY dict == {}
#JSON == {}
# процессы сериализации данных и их десесриализации

# Сериализация (запись данных в жсон- это перевод пайтон диктинори в JSON  фо
# рмат (либо сохранить в файл либо сохраняем просто как текстовые данные)


# Method
# dump - метод записывает обьект в пайтон в файл в формате JSON
#dumps - метод записывает обьект в пайтон в строку в формате JSON

# десиарлизация - (это у нас чтение данных json )
# это процесс перевода из JSON в пайтон диктинори


# load - метод который считывает файл в формате JSON и переводит его в оббекты пайтон
# loads- метод который считывает  JSON в текстовом формате и  переводит его в оббекты пайтон

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
# процесс десериализации 
# import json
# from urllib.request import urlopen 
# data = urlopen('https://randomuser.me/api/')
# print(type(data))
# # print(data) 2 cposop 
# generate_to_dict = json.load(data)
# print(generate_to_dict)
# print(type(generate_to_dict))

# import json
# with open('downApi.json', 'r')as file: 
#     data = file.read()
#     # print(data) 2
#     # print(type(data)) 2
#     user = json.loads(data)
#     print(user)
#     # print(type(user))


# Процесс сериализации 
# import json 
# dict_ = {
#     'name': 'Jhon', 
#     'last_name': 'Snow', 
#     'status': True,
#     'wife': None,
#     'children': False,
# }
# with open('new.json', 'w') as file:
#     json.dump(dict_, file)

# import json


import json


dict_ = {
    'name': 'Jhon', 
    'last_name': 'Snow', 
    'status': True,
    'wife': None,
    'children': False,
}
string = json.dumps(dict_)
print(string)
print(type(string))