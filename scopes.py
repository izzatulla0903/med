# scopes = область видимости и пространства имен 
from ast import comprehension
from distutils.command.build import build


# build - in (встроенная область видимости ) - print , len , max. int
# Clobal (глобальная область видимости )
# Enclosed (не локальная -  nonlocal )
# local (локальная область  видимости)

# def print_list(some_list): 
#     for element in some_list: 
#         print(element)
#         element = 'q'
#     print_list([1,2,3,4,5])
#     print(element)

# a = 10 #global 
# print #built - in 
# def hello(): #global 
#     a = 'hello ' # local
#     print(a, ' local inside at func')
# hello()
# print(a, 'global')
# x = 'global'
# print(x) #global 1



# def enclosed(): 
#     x = 'enclosed'
#     def local(): 
#         x = 'local'
#         print(x) #local
#     print(x) #enclosed
#     local()    
#     print(x) #enclosed
# enclosed()
# print(x) # global




# def func(): 
#     print(a)
#     a = 5  this is error , before than a
#     a = 'str'
# func()

# num = 10 
# def func(): 
#     def inner_func(): 
#         print(num)
#         inner_func()
# func()        
# var = 100 # global variable 
# def increment(): 
#     var = var + 1 #try tom update a global variBLE (USING INCREMENT - > VAR += 1)
# increment()    

# global -> позволяет менять значение глобальной переменной назодясь в локальной области видимости
# nonlocal -> позволяет менять значение не локальной переменной назодясь в локальной области видимости 

# var = 100 
# def increment(): 
#     global var
#     var += 1 
# print(var)
# increment()
# print(var)  #otvet 100 101

# def counter(): 
#     num = 0
#     def incrementer(): 
#         nonlocal num 
#         num += 1 
#         return num 
#     return incrementer 
# c = counter() 
# print(c) #<function counter.<locals>.incrementer at 0x106071550>
# print(c())  #1
# print(c()) #2           
# print(c())   #3
# c = counter()
# print(c())   #1


# print(len(dir(__builtins__))) 
# print(abs(-15)) #стандартный вызов строенной функции 
# abs = 15 #переопределяю встроенное имя в abs глобальной области
# del abs
# print(abs(-15))

#>>>>>>>>>>>>>>>>>>>>>>>[>>>>>>>>>> 
#1. [1,23], [3,3,5]] -> 6, 11 -> 11
# a = [[1,2,3], [3,3,5]]
# b = max(a, key=lambda x : x[1])[0]
# print(b)

#2
# list_ = [[1,2,3], [3,3,5]], [5,6,5], [12,3,34]
# res = max([sum(x) for x in list_])
# print(res)

# alice = [13, 15, 38]
# john = [5, 15, 50]
# def compareScores(a, i): 
#     score_a = 0
#     score_j = 0
#     for i in range(0, len(a)): 
#         if a[i] > j[i]: 
#             score_a += 1
#         elif j[i] > a[i]:
#             score_j += 1
#         else: 
#             pass 
#     return {'alice': score_a, 'john': score_j}
# print(compareScores(alice, john))
# print(compareScores([54, 20 , 10], [54, 23, 55]))



# str_= 'russ'
# dict_= {key: str_.count(key) for key in str_}
# print(dict_)



