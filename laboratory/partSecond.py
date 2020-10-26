
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

# task 10.6
def snail(): # Доделать позже
    print('Давай поможем улитке составить маршрут (ノ°益°)ノ\n')

    route = ''.join(input('Ввод символа и маршрута: ').strip().split(' '))
    counter = 0
    # for step in range(len(route)):
        # if route[step] == '>':
        #    if route[step + 1] == '>':
        # elif route[step] == '>':
        # elif route[step] == 'V':
        # else:
        
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
    
RLE()
        

