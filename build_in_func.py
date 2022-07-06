# vstroennye funccii 
# input()
# print()
# str()
# sum()
# list()
# len()
# divmod()
# globals()
# locals()
# and t.d

# map()
# filter()
# lambda
# enumerate()  


# анонимные функции это у нас lambda (это у нас такое же функции только без названия)
# lambda фунции могут принимать сколько угоднот аргументов но всегда возвращают только одно выражение 

# def sum_args(a, b): 
#     result = a +b 
#     return result 
# def sum_args1(a, b): return a + b 

# print(sum_args(1,2))
# print(sum_args(1,2))

# sum_args = lambda a, b: a * b 
# print(sum_args(218,129))


# x = lambda a,b,c: a + b + c 
# print(x(1,2,3))



# def myFunc(n): 
#     return lambda a: a * n 
# mydoubler = myFunc(2)
# mytripler = myFunc(3)
# print(mydoubler(11))
# print(mydoubler(22))
# print(mydoubler(11))
# print(mydoubler(22))

# ls = ['def', 'ivan', 'john', ' ', ' ']
# new_list = sorted(ls, key.len)
# print(new_list)



#>>>>>>>>>>>>>>>>>>>>>>>
# map(function, iterable) -> применяет функцию к каждому элементу в последовательности и возвращает mapobject
# (интератор ) с результатами


# с помощью мап можно выолнять преобразования элементов Перевести все строки в верхний регистр


# list_of_words = ['one', 'two', 'three', 'dict']
# result = list(map(str.upper, list_of_words))
# print(result)

# ls = ['1', '2', '3', '4']
# result = list(map(int, ls))
# print(result)

# names = ['john', 'jeremy', 'roma', 'sansa', 'aibek'] 
# # [hello mr/ms john or jamie]
# result = list(map(lambda x: f'hello mr/mrs {x}', names))
# print(result)

# nums = [1,2,3,4,5]
# nums2 = [100,200,300,400,500]
# #100 , 400 , 900, 1600, 2500
# result = list(map(lambda x, y: x*y, nums , nums2))
# print(result)


# dict_ = {1: 2, 3: 4, 5: 6}
#        # {1: , '2}, '3', '4', '5', '6'}
# result = dict(map(lambda items: (items[0], str(items[1])), dict_.items()))
# print(result)


#filter(function , iterable) - применяет функции ко всем элементам итерабле функци/ к которой 
# мы передаем и возвращет фильтр обжект (итератор) с теми обьектами для которых фунция вернула тру 


# list_of_str = ['one', 'two', 'list', ' ', '100', '1', '50', 'john99']
# result = filter(str.isdigit, list_of_str)
# print(list(result))
# for x in result: 
#     print(x)

# ls = [10, 11, 102, 213, 314,515]
# result = list(filter(lambda x: x % 2 != 0 ,ls))
# print(result)

# list_of_words = ['john', 'one', 'two', 'list', 'makers', 'ev.22', 'ono']
# result = list(filter(lambda x: len(x) >= 4,  list_of_words ))
# print(result)


##>>>>>>>>>>>>>>>>>>>>>>>
# enumerate(iterable) - 
# ls = ['str1', 'str2', 'str3', ]
# i = 0
# for x in ls: 
#     print(f'element: {x}, index: {i}, ')
#     i += 1 

#2 
# ls = ['str1', 'str2', 'str3', ]
# for i , x in enumerate(ls): 
#     print(f'element: {x}, index: {i}')
# new_list = list(enumerate(ls))
# print(new_list)  

# def countingValleys(n, s):

#     level=valley=0
#     for i in range(n):
#         if(s[i]=='U'):
#             level += 1
#             if(level==0):
#                 valley+=1
#         else:
#             level-=1

#     return valley
# print(countingValleys(12,'DDUUUUDD'))


#zip(iterebles) - она соединяет каждый элемент итерируемых элементов между собой в тип данных tuple 
# и возвращает его

# list1 = [1,2,3]
# list2 = [100,200,300]
# result = list(zip(list1 , list2))
# print(result)

# a = [1,2,3,4, 5]
# b = [10,20,30,40]
# c = [100,200,300]
# result = list(zip(a , b, c))
# print(result)


# zip - для создания словарей 

# d_keys = ['hostname ', 'location', 'vendor', 'model', 'ios', 'ip']
# d_values = ['london_r1', '21 new blode walk', 'cisco', '4451', '15.45', '10.255.0.1']
# dict_r1 = dict(zip(d_keys, d_values))
# print(dict_r1)

# d_keys = ['hostname ', 'location', 'vendor', 'model', 'ios', 'ip']
# data = {
#     'r1': ['london_r1', '21 new blode walk', 'cisco', '4451', '15.45', '10.255.0.1'],
#     'r2': ['london_r1', '21 new blode walk', 'cisco', '4451', '15.45', '10.255.0.2'],
#     'sw1': ['london_r1', '21 new blode walk', 'cisco', '3850', '3.6.xe', '10.255.0.1']
# }
# london_data = {}
# for key in data.keys(): 
#     london_data[key] = dict(zip(d_keys, data[key]))
# print(london_data)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# all and any 
# all -> возвращает тру если все элементы объекта истина(или объект пустой)


# ls = [False, 1, 'stroka', True ]
# print(all(ls))  


# IP = '10.255.0..1'
# result = all(i.isdigit() for i in IP.split('.'))
# print(result)

# any -> возвращает тру если хотя бы один элемент истинный 


# ls = [0, 0, ' ', False] 
# print(any(ls))



# ignore = ['rm - rf', 'alias', 'reset']
# command = 'suda rm - rf 312'
# if any([word in command for word in ignore]):
#     raise Exception('invalid command')
# print('vse ok')

#>>>>>>>>>>>>>>>>>>>>>>>>>  генератор поролей
# from random import choices 
# from string import ascii_letters, digits 
# from itertools import repeat 
# q_pass = int(input('vvedite kol-vo parolley'))
# print({
#     f(choices(ascii_letters, k=12), choices(digits, k=7)) for f in repeat(lambda  x, y: ''.join(set((x + y))),q_pass)
# })

#print(ascii_letters) вывод английского алфавита
#set перемешка всех чисел и букв в пороле

# from random import choices 
# from string import ascii_letters, digits 
# from itertools import repeat 
# q_pass = 1_000_0
# result = {
#     f(choices(ascii_letters, k=12), choices(digits, k=7)) for f in repeat(lambda  x, y: ''.join(set((x + y))),q_pass)
# }
# print(result)
# print(len)

# def foo(): 
#     var = 'peremennya foo'
#     def bar(): 
#        global var
#        var = 'peremenya bar'
#     bar()
#     print("peremennya foo:", foo)
# foo()
# print("peremenya foo: ", var)

