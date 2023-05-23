# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко 
# он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть,
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
# **Вывод:** Парам пам-пам  



 
list_poem = input("введите стих ").split()
list_vowels = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"]
list_end= []
counter = 0
 
for i in range(len(list_poem)):
     for j in range(len(list_vowels)):
         counter = counter + list_poem[i].count(list_vowels[j]) 
     if counter > 0:
         list_end.append(counter)
         counter = 0
     
 
if list(filter(lambda x: x==list_end[0] ,list_end)) == list_end:
     print("Парам пам-пам")
else:
     print("Пам парам")