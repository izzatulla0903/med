# def <name_if_function>(<a b> #parametry ):
#     <body> #некая логика некий код
#     <retern> #возвращает что-то
# <name_of_function> (<5 , 6>  # argymenty)

# параметры функции это у нас переменфе которые будут принимать наша функция 
# для того чтобы мы смогли рабатать с данными которые передаются в эту функциию


# аргументы - данные кторые мы передаем для параметров при вызове функции

#retern нужен для того чтобы функция что - то возвращала и для того чтобы мы могли работат с результатом действия функции 
#retern является не обязательными оператором то есть он нам возвращает None    если не указать  retern


# ls = []
# result = ls.append(1)
# print(ls)
# print('resultat deistvia', result)

# result1 = ls.pop()
# print(ls)
# print('resultat deistvia', result1)


# def sumTwoNums (num1,  num2 ):   #paramerty
#     result = num1+num2
#     return result 
# print(sumTwoNums(5, 5))   #argymety 

# def isEven(num):
#     if num% 2 == 0:
#         return True 
#     else:
#             return False 

# a = 10
# b = int(input('enter num: '))
# print(isEven(5))
# print(isEven(a))
# print(isEven(b))


# def isEven(num: int) -> bool:
#     """
#     наша функция проверяет является ли ччисло типа инт четным
#     """
#     if num % 2 == 0:
#         return True 
#     return False
# isEven()
# isEven1()
# dir()

#полиндромы
# def get_polindrom(words: list) -> list:
#     """
#     функция возврщает список из полиндромov
#     """
#     result = []
#     for word in words:
#       if word.lower() == word[::-1].lower():
#        result.append(word)
#        return result 
# some_words = ['john ', 'ono', 'kazak', 'Anna', 'Dovod', 'apa', 'piko']
# print(get_polindrom(some_words))

# def func():
#     print('HELLO WORLD')

#func

#default params 
# def print_welcome(name: str = 'user') -> str:
#     print(f'welcome, {name}!')
# print_welcome()




# напишите функцию которая будет возвращать ваши депозит через опраделенные время с процентом 10% возвращать финальное колво денег

# def get_procent(money: float, period: int ) -> float:
#     """
#     return final amount if money! 
#     """
#     if money < 30000:
#         raise Exception( 'вы введи неккоректное количество денег мин ставка 300000 com')

#     if period < 3:
#         raise Exception('вы введи неккоректные срок для депозита мн периол вложения 3 года ')

#     i = 0 
#     while i < period:
#         money = money + (money * 0.1)
#         # money * 1.1 / money + (money / 100 *10)
#         i += 1 # 1 = 1 + 1
#         return money 
#     money = float(input('vvedite summu deneg: '))
#     year = int(input('vvedite srok vashego depozita: '))
#     print(get_procent(money, year))


#поменять первое и последнее слово в предложении
# 1
# string = 'hello world ! my name is John , last name is Show.nice to meet you'
# lst = string.split()
# lst[-1], lst[0] = lst[0], lst[-1]
# print(' '.join(lst))

# def get_reversed_string(text: str) -> str:
#     '''return reversed string*'''
#     print(text)
#     spisok = text.split(' ')
#     print(spisok[::-1])
#     result = ' '.join(spisok[::-1])
#     print(result)
#     return result

# get_reversed_string('hello world ! my name is John , last name is Show.nice to meet you')


# def chisla(num1 , num2):
#   result = num1 + num2 
#   return result
# print(chisla(200, 500))

