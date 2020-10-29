import random

# the core file used to start laboratory task
def launch(lesson, number):
    if lesson == 0 and number == 0:
        return

# function that checks whether a string can become a number
def checkForNumber(text):
    while not str(text).isdigit() or text:
        try:
            text = float(text)
        except ValueError:
            text = input('\n - ОШИБКА#1 (ノ°益°)ノ ... Даю тебе еще шанс на исправление - ')
            continue
        break
    return int(text)

# function for re-entering in case of an error
def writeYourAnswer():
    return input('\n - ОШИБКА#2 (ノ°益°)ノ ... Даю тебе еще шанс на исправление - ')

# task 18.1 - Улыбайтесь, Господа!
def print_shrug_smile():
    print('¯_(ツ)_/¯')
def print_ktulhu_smile():
    print('{:€')
def print_happy_smile():
    print('(͡° ͜ʖ ͡°)')

# task 18.2 - Скажи 'Пароль' и проходи!
def ask_password():
    pas = 'password'
    for step in range(3):
        if input('- Попытка ввода пароля №' + str(step + 1) + ' - ') == pas:
            print(' - You\'re amazing! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧')
            return True
    print(' - Oh, shit, it\'s fail! (ᗒᗣᗕ)՞')
    return False

# task 18.3 - Золотое сечение
def golden_ratio(i):
    col = [0, 1]
    for step in range(i):
        print('Элемент №' + str(step + 1) + ' = ' + str(col[1]))
        col[0], col[1] = col[1], col[0] + col[1]
    return col[1]/col[0]

# task 18.6 - Точка на прямой
def lines(k, b, cord):
    if k * int(cord.split(';')[0]) + b == int(cord.split(';')[1]):
        return True
    return False

lines(1, 6, '1;7')
