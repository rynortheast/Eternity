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

# task 9.3
def homonyms():
    surnames = set()

    print('Узнаем кол-во однофамильцев в компании без смс и регистраци! (눈_눈)')
    workman_number = checkForNumber(input('\n - Сколько сотрудников официально трудоустроено в компании? - '))
    while workman_number <= 0:
        workman_number = checkForNumber(writeYourAnswer())
    for step in range(workman_number):
        surnames.add(input(' - Введите фамилию сотрудника №' + str(step + 1) + ': '))
    print('\nИтог! Вот столько однофамильцев присутствует в компании -> ' + str((workman_number - len(surnames)) * 2))

# task 9.2
def attendance():
    # journal = [set(input() for x in range(int(page)) for y in range(surnames_number)]

    print('Найдем же того самого студента, который посещает прям все-все пары! (눈_눈)')
    page = int(checkForNumber(input(' - Сколько страниц журнала проверяем? - ')))
    journal = list(range(page))
    for step in range(page):
        surnames_number = int(checkForNumber(input(' - Сколько студентов было в тот день? - ')))
        journal[step] = set()
        for qty in range(surnames_number):
            journal[step].add(input('- Студента №' + str(qty + 1) + ' зовут? - '))
    counter = journal[0]
    for step in journal:
        counter = counter.intersection(step)
    print('Вот эти студенты посещали все пары', *sorted(counter), sep = ' - ')

# task 10.1
def bykva():
    text = input('- Введите любой текст - ')
    number = int(checkForNumber(input('- Какую букву из текста взять? - ')))
    try:
        print('Вот твоя буква на указанной позиции - ' + text[number - 1])
    except:
        print('Увы, такой позиции в тексте нет (ノ°益°)ノ')

# task 10.3
def sayAAA():
    if (input('- Введите любой текст - ').lower().strip().startswith('а')):
        print('Oh, YES YES YES')
    else:
        print('It\'s not okay.. STOP!')
        
# task 11.1
def coin():
    kit = input('Левой-правой-левой-правой, Здрасте. Ввод набора из о и р - ')
    print('Максимальное число орлов, выпавших подряд = ' + str(len(max(kit.split('р')))))

#task 11.2
def filter():
    roster = list()
    number = int(checkForNumber(input('Занимаемся фильтром данных. Сколько слов ждать? - ')))
    for step in range(number):
        word = input('- Ввод надписи №' + str(step + 1) + ' - ').strip()
        if word.startswith('####'):
            continue
        elif word.startswith('%%'):
            roster.append(word.replace('%%', ''))
            continue
        roster.append(word)
    print(*roster, sep=' - ')

#task 11.5
def pedantry():
    word = list(''.join(input('- Ввод слова - ').strip().split(' ')))
    while len(word) >= 2:
        word = word[1 : -1]
        print(' -| ' + str(''.join(word)))

# task 12.1
def wList():
    white_list = list()
    for step in range(int(checkForNumber(input('- Какой размер белого списка? - ')))):
        white_list.append(input(' - Вввод слова №' + str(step) + ' - '))
    search = []
    for step in range(int(checkForNumber(input('\n- Сколько слов ждать? - ')))):
        search.append(input(' - Вввод слова №' + str(step) + ' - '))
    print('\nВот эти слова можно использовать: ')
    for step in search:
        if step in white_list:
            print(' - ' + str(step))

# task 12.3
def buyProduct():
    print('Добро пожаловать в наш супермаркер! (ノ°益°)ノ')
    myList = list()
    for step in range(2, checkForNumber(input('- Сколько позицей в списке? - ')) * 2 + 2, 2):
        myList.append(input('\n - Ввод товара №' + str(step // 2) + ' - '))
        myList.append(str(checkForNumber(input(' - Ввод кол-во товара - '))) + 'шт')
    print('', *myList, sep='\n')

# task 12.4
def RLE():
    sequence = input('- Ввод числовой последовательности (ノ°益°)ノ - ')
    number = int(sequence[0])
    counter = 0
    for step in range(len(sequence)):
        if number != int(sequence[step]):
            print(str(number) + ' - ' + str(counter))
            number = int(sequence[step])
            counter = 1
        elif number == int(sequence[step]):
            counter += 1
    print(str(counter) + ' - ' + str(number))
    
# task 13.1 - Напёрстки
def thimbles():
    print('Добро пожаловать в 0SkillGarbage! (≖ ͜ʖ≖) ')
    numberThimb = checkForNumber(input('- Какое кол-во напёрстников используем? - '))
    numberSwap = checkForNumber(input('- Какое кол-во перестановок делаем? - '))
    searchNumber = checkForNumber(input('- Какое число будем искать? (' + str(1) + '-' + str(numberThimb) + ') - '))
    while searchNumber > numberThimb:
        searchNumber = checkForNumber(input('- ОШИБКА! Какое число будем искать? (' + str(1) + '-' + str(numberThimb) + ') - '))
    # kodSettings = input('- Нужен ли код настройки? - ')

    game = list(range(1, numberThimb + 1))

    print('\n ~~~~~~~~~~ Да начнем нашу игру! ( ͡ᵔ ͜ʖ ͡ᵔ) ~~~~~~~~~~ \n')
    for step in range(numberSwap):
        indexs = (random.randint(0, numberThimb - 1), random.randint(0, numberThimb - 1))
        game[indexs[0]], game[indexs[1]] = game[indexs[1]], game[indexs[0]]
    
    for step in range(numberThimb):
        print(' [' + str(step + 1) + '(ʘ ʖ̯ ʘ)' + str(step + 1) + '] ', sep='', end=' ')

    print(game)
    while True:
        vibor = checkForNumber(input('\n- Твой выбор это.. - '))
        try:
            if game[vibor - 1] == searchNumber:
                break
        except:
            print(' ')
        print(' - Не повезло. Ок, пробуй еще один раз ( ͡ᵔ ͜ʖ ͡ᵔ)')
    print('Поздравляю! Ты нашёл нужное число. Игра окончена! (≖ ͜ʖ≖)')

# task 13.2 - Сортировка в обратном порядке
def revSorded():
    number = checkForNumber(input('Какое кол-во чисел ждать? - '))
    collection = list(range(number))
    for step in range(number):
        collection[step] = checkForNumber(input('- Ввод числа №' + str(step + 1) + ': '))
    collection = sorted(collection)
    collection.reverse()
    print(*collection)

# task 13.3 - A272727
def A272727():
    number = checkForNumber(input('- Какую длину последовательности ждёте? - '))
    bag = (0, 1, 0, 3, 0, 3, 0)
    col = list()
    counter = 0

    for step in range(number):
        if step + 1 <= len(bag):
            col.append(bag[step])
        else:
            for i in range(len(col)):
                if col[i] == col[0 - 1 - i]:
                    counter += 1
            col.append(counter)
            counter = 0

    if number == 0:
        print('Игра окончена, так и не начавшись! (≖ ͜ʖ≖)')
    else:
        print('Вот вся последовательность:', *col)

# task 13.6 - Большие буквы №2
def bigWord():
    text = input('- Ввод любого текста - ')
    codeChar = (' * * ***** ** *', '** * *** * *** ', ' * * **  * * * ')
    
    print('\n~ Преобразуем ваш текст в большие буквы! (≖ ͜ʖ≖) \n')
    for step in range(0, 15, 3):
        for i in range(len(text)):
            for j in range(3):
                print(codeChar[i][j + step], end='', sep='')
            print('  ', sep='', end='')
        print('')

# task 14.3 - Маяковский
def mayk():
    print(*input('@ ~ Ввод любого текста: ').split(' '), sep='\n')

# task 14.4 - Вертикальная диаграмма
def vertDiag():
    col = input('- Ввод нескольких натуральных чисел через пробел - ').split(' ')
    print('*'*(len(col) + 2), '\n*' + ' '*len(col) + '*', sep='')
    for step in range(int(max(col))):
        print('*', end='')
        for i in range(len(col)):
            if int(max(col)) - int(col[i]) - step <= 0:
                print('*', end='')
                continue
            print(' ', end='')
        print('*')


# task 15.1 - Гэтсби
def gadsby():
    bykva = input('- Введите букву, которую будем искать - ')
    words = input('- Введите предложение, в котором будем искать нужную букву - ')
    print(*[step for step in words.lower().split(' ') if str(step).find(bykva.lower()) != -1], sep='\n') 

# task 15.2 - Знаков без пробелов
def sqwn():
    text = input('- Введите любой текст - ')
    print(' - Длина текста составляет -', len(''.join(''.join(text.strip().split(' ')).split('\t'))))

# task 15.3 - Длинношееееед
def longNecked():
    word = input('- Введите слово - ')
    col = [word.count(step) for step in list(word)]
    print(' - Максимальное кол-во раз -', max(col))

# task 16.3 - Бактериям бой!
def bacteria():
    size = checkForNumber(input('- Введите размер квадратного поля - '))
    col = [[random.randint(1, 20) for step in range(size)] for step in range(size)]
    
    # print(*col, sep='\n')
    for step in range(checkForNumber(input('- Введите кол-во капель антибиотика - '))):
        x = checkForNumber(input(' - Координата x выстрела №' + str(step + 1) + ' = ')) - 1
        y = checkForNumber(input(' - Координата y выстрела №' + str(step + 1) + ' = ')) - 1
        for i in range(x - 1, x + 2):
            for k in range(y - 1, y + 2):
                try:
                    if col[i][k] - 4 <= 0:
                        col[i][k] = 0
                    else:
                        col[i][k] -= 4
                except:
                    continue
    print('', *col, sep='\n')    
def checkBacteria(one, two):
    if one - two < 0:
        return 0
    return one - two

# task 16.4 - Экономия
def economy():
    size = checkForNumber(input('- Введите размер расписания - '))
    col = [[checkStation(k, j) for j in range(size)] for k in range(size)]
    
    route = input('- Введите свой маршрут - ').split(' ')

    price = 1000
    stantion = 1000
    for step in range(size):
        if col[int(route[0]) - 1][step] == 0:
            continue
        if col[int(route[0]) - 1][step] + col[step][int(route[1]) - 1] < price:
            price = col[int(route[0]) - 1][step] + col[step][int(route[1]) - 1]
            stantion = step + 1
    print(*col, sep='\n')
    print('Пересадка через станцию №' + str(stantion) + ' - цена поездки = ' + str(price))
def checkStation(k, j):
    if k == j:
        return 0
    return random.randint(1, 9)

economy()


