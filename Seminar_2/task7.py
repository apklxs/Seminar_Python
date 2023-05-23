# dictionary = {"A": 1, "E":1, "I":1, "O":1, "U":1, "L":1, "N":1, "S":1, "T":1, "R":1, "D":2, "G":2,
#              "B":3, "C":3, "M":3, "P":3, "F":4, "H":4, "V":4, "W":4, "Y":4,"K":5, "J":8, "X":8, "Q":10, "Z":10,
#              'А': 1, 'Б': 3, 'В': 1, 'Г': 3, 'Д': 2, 'Е': 1, 'Ё': 3, 'Ж': 5, 'З': 5,
#              'И': 1, 'Й': 4, 'К': 2, 'Л': 2, 'М': 2, 'Н': 1, 'О': 1, 'П': 2, 'Р': 1,
#              'С': 1, 'Т': 1, 'У': 2, 'Ф': 10, 'Х': 5, 'Ц': 5, 'Ч': 5, 'Ш': 8, 'Щ': 10,
#              'Ъ': 10, 'Ы': 4, 'Ь': 3, 'Э': 8, 'Ю': 8, 'Я': 3}

# s = input("Введите слово состоящее из только из загланых букв английского или только русского алфавита ")
# s1 = s.upper()  
# sum = 0

# for i in range(len(s1)):
#     for (key, value) in dictionary.items():
#         if s1[i] == key:
#             sum = sum + value

# print(f"слово {s} стоит {sum} очков")

points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JZ', 10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
word = input().upper()  # переводим все буквы в верхний регистр
count = 0
for i in word:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        for j in points_en:
            if i in points_en[j]:
                count = count + j
    else:
        for j in points_ru:
            if i in points_ru[j]:
                count = count + j
print(count)