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

# Outputs the same text with input data
def horoscope(name, surname, animal, zodiac):
    print('Индивидуальный гороскоп для пользователя: ', name, ' ', surname, '\n',
        'Кем Вы были в прошлой жизни: ', animal, '\n',
        'Ваш знак зодиака - ', zodiac, '. Поэтому Вы - тонко чувствующая натура.', sep = '')

def bit_reminder():
    print('1 бит = минимальная единица количества информации. \n',
        '1 байт = 8 бит \n',
        '1 Килобит = 1024 бита. \n',
        '1 Килобайт = 1024 байта. \n',
        '1 Килобайт = ', 1024 * 8, ' бит.', sep = '')

def reverse_parrot(message):
    message.reverse()
    for word in message:
        print(word)
        

launch(1, 3)