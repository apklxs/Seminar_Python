from func import *
from interface import *

print("Программа для работы с текстовым файлом \nсодержащим ФИО и номер телефона.\n")
file = "bd.txt"
number = interface()
# readfile(file)

while number != 6:
    if number == 1:
        lastname = input("Введите Фамилию для добавления ") 
        firstname = input("Введите Имя для добавления ") 
        threename = input("Введите Отчество для добавления ")
        numbertel = input("Введите номер телефона для добавления ")
        addcontactinfile(lastname +" "+ firstname +" "+ threename +" "+ numbertel,file)
        number = interface()
    elif number == 2:
        readfile(file)
        number = interface()
    elif number == 3:
        lastname = input("Введите для поиска Фамилию или ее часть с учетом регистра ") 
        findinfile(lastname,file)
        number = interface()
    elif number == 4:
        numberstr = input("Введи номер записи для удаления, внимание список будет перенумерован ") 
        if int(numberstr) <= quantstrigfile(file):
            delstrinfile(numberstr,file)
            checknumerentry(file)
        else:
            print("Нет такой запси для удаления")
        number = interface()
    elif number == 5:
        numberstr = input("Введи номер записи для изменения ") 
        if int(numberstr) <= quantstrigfile(file):
            lastname = input("Введи фамилию ")
            fierstname = input("Введи имя ") 
            threename = input("Введи отчество ")
            numbertel = input("Введи номер телефона ")
            changefile(fierstname,lastname,threename,numbertel,numberstr, file)
            checknumerentry(file)
        else:
            print("Нет такой запси для изменения")
        number = interface()
 





