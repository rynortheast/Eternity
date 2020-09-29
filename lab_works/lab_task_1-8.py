import random

# the core file used to start laboratory task
def launch(lesson, number):
    if lesson == 1 and number == 1:
        name = input('Ваше имя: ')
        surname = input('Фамилия: ')
        animal = input('Любимое животное: ')
        zodiac = input('Ваш знак зодиака: ')
        horoscope(name, surname, animal, zodiac)
    elif lesson == 1 and number == 2:
        bit_reminder()
    elif lesson == 1 and number == 3:
        message = input('Обратный попугай, повторяй за мной: ')
        reverse_parrot(message.split(' '))

# task 1.1
def horoscope(name, surname, animal, zodiac):
    print('Индивидуальный гороскоп для пользователя: ', name, ' ', surname, '\n',
        'Кем Вы были в прошлой жизни: ', animal, '\n',
        'Ваш знак зодиака - ', zodiac, '. Поэтому Вы - тонко чувствующая натура.', sep = '')

# task 1.2
def bit_reminder():
    print('1 бит = минимальная единица количества информации. \n',
        '1 байт = 8 бит \n',
        '1 Килобит = 1024 бита. \n',
        '1 Килобайт = 1024 байта. \n',
        '1 Килобайт = ', 1024 * 8, ' бит.', sep = '')

# task 1.3
def reverse_parrot(message):
    message.reverse()
    for word in message:
        print(word)

# --------------------------------------------------------------------------------------- #

# task 2.1
def checkInt():
    message = input('- Куда идем? (1-5): ')
    while not message.isdigit():
        message = input('\n Некорректно. Куда идем? (1-5): ')
    return int(message)

def maze():
    end = False
    attempt = 0
    cave = list(range(10))
    ui_cave = '[‾‾]  '

    lucky = 0
    
    for step in range(10):
        cave[step] = random.randint(1, 4)
        print(cave[step], end=', ')

    while end == False:
        if attempt != 0:
            print('\n oh, shit, here we go again') # Позже необходимо поменять фразу
        for step in cave:
            print('\n' * 2, ui_cave * 5, end='', sep='')
            if checkInt() == step:
                print('\n Вы проходите дальше :)')
                continue
            attempt += 1
            break


maze()

# task 2.2
def mail_registration():
    while True:
        login = input('Логин: ')
        email = input('Резервная почта: ')
        if login.find('@') != -1 or not login:
            print('Некорректный логин. Попробуйте еще раз. \n')
            continue
        elif email.find('@') == -1:
            print('Некорректная резервная почта. Попробуйте еще раз. \n')
            continue
        break
    print('Ok')

# task 2.3
def schizophrenia():
    print('О, привет!')
    answer = input('Как дела? Как настроение? \n - ')
    if answer.find('хорош') != -1 or answer.find('прекра') != -1:
        print('Отлчично. У меня тоже все классно („• ֊ •„)')
    elif answer.find('плохо') != -1  or answer.find('грустно') != -1:
        print('Печально, но главное не переживай. Скоро все будет супер ⊂( ´ ▽ ` )⊃')
    else:
        print('моя твоя не понемать, брат')

# task 2.4
def da_or_net():
    first = input('#1 - Да или Нет: ')
    second = input('#2 - Да или Нет: ')
    if first.lower() == 'да' or first.lower() == 'нет':
        if second.lower() == 'да' or second.lower() == 'нет':
            print('Верно!')
            return
    print('Неверно!')

# task 2.5
def personality_test():
    print('temporarily not working :(')

# --------------------------------------------------------------------------------------- #

# task 3.1
def plus_or_minus():
    try:
        number = float(input('Любое дробное число - '))
    except:
        print('Некорректное дробное число!')
        return
    if float(number) > 0:
        print('+')
    elif float(number) < 0:
        print('-')
    else:
        print('0')