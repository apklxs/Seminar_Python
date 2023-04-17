# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
import random
print("Задача 5 Вычисляет сколько раз содержится натуральное число X в массиве из N натуральных чисел ")

def checkInputInt(s):
    p = (input(f"{s}"))
    while p.isdigit() != True or int(p) <= 0:
        print("Вы ввели не целое положительное число")
        p = (input(f"{s}"))
    return int(p)


n = checkInputInt("Введите число элементов массива \n")
list_1 = list()

for i in range(n):
    list_1.append(random.randint(0, 99))

print(f"сгенерирован массив {list_1}")

x = checkInputInt("Введите число для поиска \n")
count = 0

for i in range(n):
    if x == list_1[i]:
        count = count + 1

print(f"число {x} содержится в массиве {count} раз")







