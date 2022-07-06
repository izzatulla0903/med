from itertools import product
import json
import random
from secrets import choice

FILE_PATH = 'data.json'

def get_data(): 
    with open(FILE_PATH) as file:
        return json.load(file)
def list_of_products():
    data = get_data()
    return data

def retrieve_data(): 
    data = get_data()
    # print(data,'------') 2
    id = int(input('vvedite id producta: '))
    product = list(filter(lambda x: x['id'] == id, data))
    return product[0]

# print(retrieve_data()) 2
# def create_data():
#     data = get_data()
#     with open('id.txt', 'r') as file:
#         id = int(file.read())
#         # print(id)
#         # print(type(id))
#         id += 1
#     with open('id.txt', 'w') as file :
#         file.write(str(id))
# create_data()
def get_id():
     with open('id.txt', 'r') as file:
        id = int(file.read())
         
        id += 1
     with open('id.txt', 'w') as file :
      file.write(str(id))
      return id 
def create_product():
    data = get_data()
    product = {
        'id': get_id(), 
        'title': input('vvedite nazvanie producta: '),
        'price': int(input('vvedite price producta: ')),
        'description': input('vvedite opisanye: ')
    }
    data.append(product)

    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
    result = {'msg': 'created', 'product': product}
    return result

# print(create_product())  2 добавляем продукт в список ввыше код
def update_product():
    data = get_data()
    flag = False
    id = int(input('vvedite id producta: '))
    product = list(filter(lambda x: x['id'] == id, data))
    
    if not product:
        return {'msq': 'invalid id! product does not exist!'}
    index  = data.index(product[0])
    choice = input('chto izmenite\'?(ttitle-1, price-2, description-3: ')
    if choice == '1':
        data[index]['title'] = input('vvedite new name: ')
        flag = True
    elif choice == '2':
        data[index]['price'] = float(input('vvedite new price: '))
        flag = True
    elif choice == '3':
        data[index]['description'] = input('vvedite new opisanye: ')
        flag = True
    else:
        print('invalid choice to update!!!')

    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
    if flag:
        return {'msg': 'updated', 'product':
        data[index]}
    else:
        return {'msg': 'not UPDATE!'}
def delete_product():
    data = get_data()
    id = int(input('vvedite id producta: '))
    product = list(filter(lambda x: x['id'] == id, data))
    if not product:
        return {'msq': 'invalid id! product does not exist!'}
    index = data.index(product[0])
    deleted = data.pop(index)

    json.dump(data, open(FILE_PATH, 'w'))
    return{'msg': 'deleted!', 'product': deleted}

        