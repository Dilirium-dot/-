# words = ["радиостанция", "калиграфия", "калейдоскоп", "пастила", "крокодил", "рентген", "рентгеноэлектрокардиография", "водогрязеторфопарафинолечение", "опоссум", "лололошка точка невозврата 71", "мультимедиавидеоконтроллер", "скриптонит", "патологоанатом", ""]
import random
f = open('words.txt')
words = (f.read().split(', '))
word = words[random.randint(0, len(words)) - 1].encode('cp1251').decode('utf-8')
vis = '*' * len(word)
word_list = list(word)
vis_list = list(vis)
count = 0
print(vis)
while True:
    count += 1
    ans = input("Введите букву: ")
    if ans in word:
        print('Есть такая буква')
        for i in range(0, len(word_list)):
            if word_list[i] == ans:
                vis_list[i] = ans
    else:
        print('Нет такой буквы')
    print(''.join(vis_list), 'Попытка', count)
    if '*' in vis_list:
        continue
    else:
        break
