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
cave = list(range(10))
ui_cave_door_left = '┬┴┬┴┤ '
ui_cave_door_right = ' ├┬┴┬┴'
ui_cave_sten = '┬┴┬┴┬┴┬┴┬┴┬┴┬'

def checkInt(step):
    message = input(' - Куда идем? (1-' + str(step) + '): ')
    while not message.isdigit():
        message = input('\n Некорректно. Куда идем? (1-5): ')
    return int(message)

def regenCave(number):
    room = 0
    print(' ')
    while number > room:
        room = random.randint(2,5)
    was = room
    rty = 1
    for step in range(5):
        if was == (5 - step):
            print(ui_cave_door_left, rty, ui_cave_door_right,end='', sep=' ')
            rty += 1
            was -= 1
            continue
        elif was == 0:
            print(ui_cave_sten, end='', sep='')
            continue
        elif (random.randint(0,1)):
            print(ui_cave_door_left, rty, ui_cave_door_right,end='', sep=' ')
            rty += 1
            was -= 1
            continue    
        print(ui_cave_sten, end='', sep='')
    return room

def maze():
    end = False
    attempt = 0
    level = 1
    # lucky = 0 - Параметр, отвечающий за удачу игрока, который влияет на исход игры
 
    for step in range(10):
        cave[step] = random.randint(1, 4)
        print(cave[step], end=', ')

    # Starting a greeting
    print('\n \n')
    print('Oh, no, you\'re lost in a cave! You need to get out of here..(')
    print('ヽ(`⌒´メ)ノ Are you ready? Let\'s go! ~ ~ ~ ~ ~ ~ \n')

    while not end:
        if attempt != 0:
            print('\n __________________________________________________________________________________\n ')
            print(' - oh, shit, here we go again') # Позже необходимо поменять фразу.
            print(' - It looks like you\'ve returned to your starting location. Let\'s try again (눈_눈)')
        for step in cave:
            # if random.randint(1, 5) == 2: - Дополнитекльный функционал. Побочные действия, влияющий на итог игры.
            if level == 11:
                end = True
                break
            if checkInt(regenCave(step)) == step:
                print('\n - Great! You have come to the location with the number ' , level, ' ᕕ( ᐛ )ᕗ', sep='')
                level += 1
                continue
            attempt += 1
            level = 1
            break

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