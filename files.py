#работа с файлами
# каретка - указатель
#open(<путь до вашего  файла >)
# file = open('/home/sanzhar/Desktop/ev22/files/failes.py') #абосолютный путь
# file = open('files.py')  #относительный путь
# print(file)

# режимы длЯ работы с файлами 
# 1. r/r+  (read)
# 2. w/w+  (whrite)
# 3. a/a+ (append)
# t, b , x

# file = open('text.txt', 'r')
# data = file.read()
# data = data.split('\n')
# print(data) 
# print(type(data))
# file = open('/home//Desktop/ev22/files/failes.py ')
# data = file.readlines()
# print(data)


# file = open('text.txt', 'w')
# file.white('hello world\nmy name is john snow\nking!')
# file.close()


# file = open('text.txt', 'a')
# file.write('\nJOhn snow bastard and king')
# file.close()


# file = open('text1.txt', 'w')  #создает файл
# file.close()

# ls = ['hello world', 'my name is john', 'i\'m 35 years old']
# with open ('text.txt', 'w') as f: 
#     f.writelines(line + 'n' for line in ls)


# file.tell() -> возвращает инлекс где находится каретка(указатель)
# file seek (<int>) -> перемещает каретку (указатель) на указанный инт(индекс)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# from PIL import Image 
# import pytesseract 
# import re
# def get_imei_codes(list_images): 
#     list_of_imei = []
#     for image in list_images:
#         string = pytesseract.image_to_string(image)
#         print(string)
#         list_of_imei.append(re.findall(r'IME.\d.\s\d+', string))
#         print(list_of_imei)

#     with open('imeicodes.txt', 'w') as file:
#         for x in list_of_imei:
#             for i in x:
#                 file.write(f'{i}\n')


# list_images = ['imei.jpg']
# get_imei_codes(list_images)


# a = int(input('vvedite 1 :'))
# b = int(input('vvedite 2:'))
# c = int(input('vvedite 3:'))
# d = int(input('vvedite 4: '))
# if a >= b and a >= c and a >= d:
#     print(a)
# elif b >= a and b >= c and b >= d:
#     print(b)
# elif c >= a and c >= b and c >= d:
#     print(c)
# else:
#     print(d)


#>>>>>>>>>>>>>>>>>>>>>
