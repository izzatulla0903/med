# обработка исключений 
#оперыторы try ....except

#ошикбки связанные с кодом 



# SyntaxError
# IndentationError
# TabError

# #исключения - invalid Values
# ZeroDivisionError
# ArithmeticError
# NameError
# IndexError
# KeyError
# ValueError
# ImportError
# BaseException #проподитель всех ошибок


# try:
#     <body try>
# except:
#     <body except>


# nam1 = int(input('vvedite chiclo'))
# print(nam1)
# print('ochen vazhnaya ctochka')
# try: 
#     nam1 = int(input('vvedite chiclo'))
#     print(nam1)
# except:
#      print('vy vveli nekorek dannye , correct its')
# print('pchen vazhnay croka koda')

# import sys
# list_ = [1,2,3,4,5,]
# index = int(input('vvedite index'))
# try:
#     res = list_[index]
#     print(res)
# except:
#     import sys
#     print('oops , we catched {sys.exc_info() [0]} error!')
#2 exception 
# list_ = [1,2,3,4,5,]
# index = int(input('vvedite index'))
# try:
#      res = list_[index]
#      print(res)
# except Exception as e:
#     print(f'oops,  we catched {e} error')

# list_ = [1,2,3,4,5,]

# try:
#       index = int(input('vvedite index'))
#       res = list_[index]
#       print(res)
# except IndexError:
#     print(IndexError)
# except ValueError: 
#     print(ValueError)

#else в try .. except
# try:
#     <body>
# except:
#     <body>
# else:
#     <body> #если в операторе трай не случится ошибка

# finally:   #срабатывает при любом исходе 
#     <body> 

# try:
#     num1 = int(input('enter: '))
#     num2 = int(input('enter: '))
#     result = num1 / num2 
# except ZeroDivisionError:
#     print('na nol delit nelzya')
# except ValueError:
#     print('invalid symbols')
# else:
     
#      print(result)
# finally:
#     print('kod zakomchils')







#дз с файлами!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 1.file = open("task.txt", encoding='utf-8')

# print(file.read(9))







# file = open('task.txt', 'a')
# file.write('1 ')
# file.write('2 ')
# file.write('3 ')
# file.write('4 ')
# file.write('5 ')
# file.write('6 ')
# file.write('7 ')
# file.write('8 ')
# file.write('9 ')
# file.write('10')
# file.close()


#4$$$ file = open('task.txt',encoding='utf-8' )
# print(file.read())
# fname = input('vvedite name file: ')
# operate = open(fname)
# count = 0
# for line in operate:
#     count = count + 1
# print(count)


#5file = open("task.txt", encoding='utf-8')
# print(file.read())
# integers = open('task.txt', 'r') 
# largestInt = 0 
# smallestInt = 1
# for line in integers:
#     if largestInt <= int(line.strip()): 
#         largestInt = int(line.strip()) 
#     if smallestInt >= int(line.strip()): 
#         smallestInt = int(line.strip()) 
# integers.close() 
# print ("Smallest = ", smallestInt)
# print ("Largest = ", largestInt)




# extra 2file = open('task.txt')

# lines = 0
# words = 0
# symbols = 0

# for line in file:
#     lines += 1
#     words += len(line.split())
#     symbols += len(line.strip('\n'))

# print("Lines:", lines)
# print("Words:", words)
# print("Symbols:", symbols)

# extra 3# with open("task.txt") as file:

#     counter = summa = 0
#     for line in file:
#         counter += 1
#         length_line = len(line)
#         for i in range(length_line):
#             if line[i].isdigit():
#                 num = int(line[i])
#                 summa += num
#                 if num < 3:
#                     print("Ученик(ца) у которого средний бал по классу меньше 3-х:", line)
#                 break
 
#     sred = counter // summa
#     print("\nСредний бал по классу:", sred)
    

# file = open('text.txt', 'a')  #extra 1
# file.write(input('vvedite words: '))
# file.close()