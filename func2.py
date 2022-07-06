# def sum_of_args(a: int, b: int, c: int, d: int) -> int: # a, b, c , d parametry
#     '''returns sum of all parameters'''
#     return a + b + c + d 
# result = sum_of_args
# print(result)
# print(type(result))
# print(result(5, 10 , 15 , 20))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#позиционные и именованные аргументы 

# def printParams(a,b,c):
#     print(a, 'is stored in param a')   #default =None
#     print(b, 'is stored in param b')
#     print(c, 'is stored in param c')
# printParams(5, 2, 3) 


# def sum_of_args(a: int, b: int, c: int, d: int) -> int: # a, b, c , d parametry
#     '''returns sum of all parameters'''
#     return a + b + c + d 
# print(sum_of_args(1,2,3,4)) #позиционные аргументы (arguments)
# print(sum_of_args(a=5, b=6, d=7, c=6))
# #именованные аргументы (key arguments)
# print(sum_of_args(5 , 10 , d= 15 , c=6))


#>>>>>>>>>>>>>>>>
#operator *  можно распакоывавать переменные 
# a = [1,2,3]
# b = [4,5,6]
# c = [*a, *b]
# print(c)
# print(*a, end='*')   #end добавляет в конце что вы напишите

#>>>>>>>>>>>>>>>>
# *args **kwargs  в функциях  распаковка именованных и позиционных

# def print_scores(student, *scores):
#     print(f'student name: {student}')
#     # print(args)
#     # print(type(args))
#     for x in scores:
#       print(f'ocsenka:'x)
# print_scores('john snow', 90, 80, 70, 60 ,50) 

# def print_pet_names(owner, **pets):   #кварц или же две звездочки перемещают к себе аошкменты даже если ее нет 
#     print(f'owner name: {owner} ')
#     # print(pets)
#     # print(type(pets))
#     for pet , name in pets.items():
#         print(f'{pet}: {name}')
# print_pet_names('John Snow', dog='rex', cat='Larry', fish=['Nemo','dori', 'Alex'] )

# def get_some_data(a, b, *args, **kwargs):
#     print('parametry a and b: ', a, b)
#     print(args[0])
#     print(args[-1])
#     print(kwargs['name'])
#     print('argumets:', args)
#     print('immenovanyye arguments: ', kwargs)
# get_some_data(1,2,3,4,5, lang = 'python', name='John Snow', car='Bmw')
    

# def conc_two_string(str1, str2):
#     import random 
#     res = random.randit(1,10)
#     return str1 + str2 + str(res)
# result = conc_two_string('hello', 'world')
# print(result)
# def generate_password(name, fam): 
#     import random 
#     random_num = random.randint(100000, 999999)
#     return name + fam + '_' + str(random_num)
# def get_info():
#     name = input('vvedite imia: ')
#     fam = input('vvedite fam: ')
#     return generate_password(name, fam)
# result = get_info()
# print(result)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>
# def generate_random_string(len_, lang):
#     import string as s
#     import random 
#     random_str = ' '.join(random.choice(s.ascii_lowercase + s.digits) for i in range(0, len_))
#     return random_str 

# print(generate_random_string(15, 'eng'))




#>>>>>>>>>>>>>>>>>>>>>>>>>>>



# def add(num1, num2): return num1 + num2
# def subtract(num1, num2): return num1 - num2
# def multiply(num1, num2): return num1 * num2
# def divide(num1, num2):
#     try:
#         return num1 / num2 
#     except ZeroDivisionError:
#         return 'na 0 delit\' nel\'zya!'
# def main():
#     try: 
#      num1 = float(input('vvedite pervoe chislo: '))
#      num2 = float(input('vvedite vtoroe chiclo: '))
#     except ValueError:
#         main()
#         print('vy vveli nekkorektnoe')
#     operator = input('vvedite operator(+, -, /, *): ')
#     result = None

#     if operator == '+': result = add(num1, num2)
#     elif operator=='-': result = subtract(num1, num2)
#     elif operator=='*': result = multiply(num1, num2)
#     elif operator=='/': result = divide(num1, num2)
#     else: 
#         print('vy vveli nekkorectnyi operator')
#         print(f'resultat: {result}')  
#         qestion = input('hotite prodolzhit\'?(yes/No): ')
#         if qestion.lower() == 'yes' :
#             main()
#         else: 
#             print('thanks for using us calculator, BYE BEY!!! ')
# main()   
# from functools import reduce
# ls = ['iizzat', 'max', 'masha']
# print(reduce(lambda x, y: x if len(x) > len(y) else y, ls))
