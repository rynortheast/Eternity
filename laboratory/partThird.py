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

# task 19.1 - Месяц / Month
def month_name(number, lang):
    col = {
        'rus':{
            1:'Январь',
            2:'Февраль',
            3:'Март',
            4:'Апрель',
            5:'Май',
            6:'Июнь',
            7:'Июль',
            8:'Август',
            9:'Сентябрь',
            10:'Октябрь',
            11:'Ноябрь',
            12:'Декабрь'
        },
        'en':{
            1:'January',
            2:'February',
            3:'March',
            4:'April',
            5:'May',
            6:'June',
            7:'July',
            8:'August',
            9:'September',
            10:'October',
            11:'November',
            12:'December'
        }
    }
    return col[lang][int(number)]

# task 19.2 - Ход конём
def possible_turns(k):
    bykva = 'ABCDEFGH'.find(k[0])
    col = [
        (bykva + 1, int(k[1]) + 2),
        (bykva + 2, int(k[1]) + 1),
        (bykva + 2, int(k[1]) - 1),
        (bykva + 1, int(k[1]) - 2),
        (bykva - 1, int(k[1]) - 2),
        (bykva - 2, int(k[1]) - 1),
        (bykva - 2, int(k[1]) + 1),
        (bykva - 1, int(k[1]) + 2),
    ]
    return sorted(['ABCDEFGH'[step[0]] + str(step[1]) for step in col if step[0] >= 0 and step[1] > 0 and step[0] < 8 and step[1] < 8])

# task 19.4 - Палидромы
def palidrom(stroka):
    rev_stroka = list(stroka.lower())
    rev_stroka.reverse()
    if ''.join(rev_stroka) == stroka.lower():
        return '- Палидром'
    return '- Не Палидром'



