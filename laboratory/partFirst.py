import random
import time

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
    elif lesson == 2 and number == 1:
        maze()
    elif lesson == 2 and number == 2:
        mail_registration()
    elif lesson == 2 and number == 3:
        schizophrenia()
    elif lesson == 2 and number == 4:
        da_or_net()
    elif lesson == 3 and number == 1:
        plus_or_minus()
    elif lesson == 3 and number == 2:
        calculator()
    elif lesson == 3 and number == 3:
        leap_years()
    elif lesson == 3 and number == 4:
        asunder()
    elif lesson == 3 and number == 5:
        layout()
    elif lesson == 3 and number == 7:
        beautiful_numb()
    elif lesson == 3 and number == 9:
        telegrams()
    elif lesson == 4 and number == 1:
        stroki()
    elif lesson == 4 and number == 4:
        vkPassword()
    elif lesson == 4 and number == 5:
        syracuse()
    elif lesson == 4 and number == 8:
        guessing_game()
    elif lesson == 5 and number == 2:
        circus()
    elif lesson == 5 and number == 3:
        nim()
    elif lesson == 6 and number == 1:
        reverse_report()
    elif lesson == 6 and number == 2:
        pyramid()
    elif lesson == 7 and number == 1:
        find_cat()
    elif lesson == 7 and number == 2:
        find_cat_v2()
    elif lesson == 7 and number == 3:
        find_cat_v3()
    elif lesson == 8 and number == 1:
        division_table()
    elif lesson == 8 and number == 2:
        haha_draw()
    else:
        print('\n- Задание не найдено (눈_눈)')

    

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

# --------------------------------------------------------------------------------------- #

# task 3.1
def plus_or_minus():
    try:
        number = float(input('Любое дробное число - '))
    except:
        print('Некорректное дробное число!')
        return
    if number > 0:
        print('+')
    elif number < 0:
        print('-')
    else:
        print('0')

# task 3.2
def calculator():
    while True:
        try:
            number_1 = float(input('Ваше первое число - '))
            number_2 = float(input('Ваше второе число - '))
        except:
            print('\n- Некорректное число. Попробуйте еще раз!')
            continue
        sign = input('Какое действие выполнить? - ')
        break
    if sign == '+':
        print('Ответ -', number_1 + number_2)
    elif sign == '-':
        print('Ответ -', number_1 - number_2)
    elif sign == '*':
        print('Ответ -', number_1 * number_2)
    elif sign == '/':
        print('Ответ -', number_1 / number_2)
    else:
        print('888888 - еррор (눈_눈)')

# task 3.3
def leap_years():
    year = str()
    while not year.isdigit():
        year = input('Какой год желаете проверить? - ')
        if not year.isdigit():
            print('\n- Ошибка ввода. Попробуйте еще раз! ')
            continue
    if int(year) % 4 == 0 and int(year) % 100 != 0:
        print('- Високосный')
    elif int(year) % 400 == 0:
        print('- Високосный')
    else:
        print('- Не високосный')

# task 3.4
def asunder():
    number = int(input('Введите любое число - '))
    if number % 2 == 1:
        print('- Нечетное')
    else: 
        print('- Четное')

# task 3.5
def layout():
    print('Let\'s try the veteran layout method (´･ᴗ･ ` )')
    name = input('- Введите своё имя: ')
    print('Лучшая длина -:', len(name) * 2 + 3)

# task 3.7
def beautiful_numb():
    number = input('Какое число тестируем? - ')
    while len(number) != 3 or not number.isdigit():
        number = input('\n- Ой, какая-то ошибка! Попробуй еще раз (눈_눈) - ')
    if (int(number[0]) + int(number[2])) / 2 == int(number[1]):
        print('Ого! Вы ввели красивое число ~ ~ ~')
        return
    print('Жаль! Ваше число не такое красивое как 468 (눈_눈)')

# task 3.9
def telegrams():
    text = input('Один символ = 40 копеек. Напиши и посчитаем! - ')
    print('- Твое сообщение стоит нам: ', len(text) * 40 // 100, 'р. ', len(text) * 40 % 100, 'коп. ', sep='')

# --------------------------------------------------------------------------------------- #

# task 4.1
def stroki():
    text = str()
    word = str()
    print('Добро пожаловать! Я программа-психотерапевт. Что расскажите? ヽ(°〇°)ﾉ \n')
    while word != 'Спасибо.':
        print(len(word))
        text += word
        print(len(text))
        word = input('- ')
    print(len(text + word))

# task 4.4
def vkPassword():
    print('Необходимо придумать пароль |ʘ‿ʘ)╯')
    while True:
        pass_1 = input('- Новый пароль: ')
        if len(pass_1) < 8:
            print('\nВаш пароль короткий! Попробуйте еще раз.')
            continue
        elif pass_1.isalpha() or pass_1.isnumeric():
            print('\nВаш пароль простой! Попробуйте еще раз.')
            continue
        pass_2 = input('- Повторите пароль: ')
        if pass_1 != pass_2:
            print('\nПароли различаются! Попробуйте еще раз.')
            continue
        print('Поздравляю! Пароль создан |ʘ‿ʘ)╯')
        break

# task 4.5
def syracuse():
    counter = 0
    number = input('- Введите стартовое число: ')
    while not number.isdigit():
        print('\nВарнинг! Попробуйте еще раз.. o/')
        number = input('- Введите стартовое число: ')
    number = int(number)
    while number != 1:
        print(int(number), end=' -> ')
        if number % 2 == 0:
            number = number / 2
        else:
            number = 3 * number + 1
        counter += 1
    print(int(number), end='')
    print('\nХодов до единицы -', counter)
    
# task 4.8
def guessing_game():
    reply = str()
    numb_1 = 1
    numb_2 = 1000
    counter = 0

    print('Бинарная угадайка! Загадай число от 1 до 1000 (ಠ‿ಠ)\n')
    while reply != '=':
        step = random.randint(numb_1, numb_2)
        reply = input('- Как насчет этого числа: ' + str(step) + ' - ')
        if reply == '=':
            numb_2 = step
            break
        elif reply == '>':
            numb_2 = step - 1
        elif reply == '<':
            numb_1 = step + 1
        else:
            print('\n Оу, вы вели что-то непонятное! Попробуйте еще раз.')
            continue
        counter += 1
    print('Ура! Вот и наш ответ:', numb_2, '\nУгадано за', counter, 'попыток!')

# --------------------------------------------------------------------------------------- #

# task 5.2
def circus():
    counter = 0

    number = int(input('Какое кол-во камней необходимо? - '))
    while number != 1:
        if number % 2 == 1:
            number -= 1
        else:
            number /= 2
        counter += 1
    print('- Необходимо сделать ' + str(counter) + ' действий!')

# task 5.3
def nim():
    heap = list(range(2))
    heap[0] = int(input('Кол-во камней в куче №1: '))
    heap[1] = int(input('Кол-во камней в куче №2: '))
    while heap[0] != 0 or heap[1] != 0:
        select = int(input('\n- Выберите кучу: '))
        count = int(input('- Сколько забираете? - '))
        while heap[select - 1] - count < 0:
            count = int(input('- Ошибка! Столько забрать невозможно.. Сколько? - '))
        heap[select - 1] = heap[select - 1] - count
        print('Куча №1 имеет - ' + str(heap[0]) + ' камней!')
        print('Куча №2 имеет - ' + str(heap[1]) + ' камней!')
    print('\nИгра окончена! Камней больше нет (ಥ﹏ಥ)')

# task 5.4
# task 5.5 - Стоит сделать эти задания, как появится возможность!

# --------------------------------------------------------------------------------------- #

# task 6.1
def reverse_report():
    times = int(input('Даешь отчёт! Стартовое значение? - '))
    for step in range(times):
        print('Осталось секунд - ' + str(times - step))
        time.sleep(1)
    print('Пуск!')

# task 6.2
def pyramid():
    num = int(input('Боб-строитель на связи! Какова высота пиромиды? - '))
    for step in range(num):
        print(" " * (num - step), "*", "*" * 2 * step, " " * (num - step), sep='')

# --------------------------------------------------------------------------------------- #

# task 7.1
def find_cat():
    message = str()
    print('Боже, нужно срочно найти кота! Зачем?! Без лишних вопросов (ノ°益°)ノ')
    counter = int(input('- Сколько строк необходимо? - '))
    for step in range(counter):
        message += input('Ввод строки №' + str(step + 1) + ' - ')
    if message.lower().find('кот') != -1:
        print('- МЯУ')
    else:
        print('- ~ТИШИНА')

#task 7.2
def find_cat_v2():
    message = str()
    step = str()
    counter = 1
    catFind = -1
    print('- Господи! Этот комок шерсти снова куда-то пропал.. НАЙДИ ЕГО! (ノ°益°)ノ')
    while step != 'стоп':
        message += step
        step = input('Ввод строки №' + str(counter) + ' - ').lower()
        if step.find('кот') != -1:
            catFind = counter
        counter += 1
    if catFind != -1:
        print('- Кот найден в строке №' + str(catFind) + ' - МЯУ')
    else:
        print('- ~ТИШИНА')

#task 7.3
def find_cat_v3():
    message = str()
    print('ААА, ХВАТИТ! Вот куда он снова делся! АА, ИЩИМ! (ノ°益°)ノ')
    counter = int(input('- Сколько строк необходимо? - '))
    for step in range(counter):
        message += input('Ввод строки №' + str(step + 1) + ' - ')
        if message.lower().find('кот') != -1:
            print('- Ух, нашелся - МЯУ')
            break
        else:
            print('- ~ТИШИНА')
    return

# --------------------------------------------------------------------------------------- #

#task 8.1
def division_table():
    print('Программа для создания таблицы деления! (눈_눈)')
    colums = int(input('- Введите кол-во столбцов: '))
    lines = int(input('- Введите кол-во строк: '))

    for step_one in range(lines):
        print('')
        for step_two in range(colums):
            print(round((step_two + 1) / (step_one + 1), 1), end='   ')
    print('\n\nНеобходимая таблицу создана. Поздравляю! (눈_눈)')

#task 8.2
def haha_draw():
    print('Просто рисую прямоугольники разными символами! HELP ME! (눈_눈)')
    heigh = int(input('- Введите высоту фигуры: '))
    width = int(input('- Введите ширину фигуры: '))
    sign = input('- Каким символом рисуем? - ')

    for step in range(heigh):
        if step == heigh - 1 or step == 0:
            print(sign * width)
        else:
            print(sign, ' ' * (width - 2), sign, sep='')
    
    print('\nПрямоуголник из ' + sign + ' построен. Размер ' + str(width) + 'x' + str(heigh) + '. Спасибо!')

lesson = int(input('- Номер урока: '))
quest = int(input('- Номер задания: '))
print('Поиск задания.. ᕕ( ᐛ )ᕗ \n')

launch(lesson, quest)