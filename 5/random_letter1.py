import random
a = ['Привет', 'Самовар', 'Гидроэлектростанция']
b = random.randint(0,len(a) - 1)
c = random.randint(0,len(a[b]) - 1)
print(a[b][0:c] + '?' + a[b][c + 1::])
if input('Введите букву пропущенную букву \n') == a[b][c]:
    print(f'Победа!\nСлово: {a[b]}')
else: 
    print(f'Попробуйте в другой раз \nслово: {a[b]}')


'''Задан список слов. Необходимо выбрать из него случайное. Из выбранного случайного слова случайно выбрать букву и попросить 
пользователя ее угадать.

Задан список слов: [‘самовар’, ‘весна’, ‘лето’]
Выбираем случайное слово: ‘весна’
Выбираем случайную букву: ‘с’
Выводим на экран: ве?на
Пользователь пытается угадать букву.
'''