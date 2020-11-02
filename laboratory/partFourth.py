from PIL import Image, ImageDraw
import random

# task 25.1 - Генератор паролей v.1
def generator_password(length):
    col = []
    for step in range(length):
        number = random.randint(28, 122) * ((step + 1) / (step + 1))
        while number in range(91, 97) or number in range(58, 65) or chr(number) in col:
            number = random.randint(28, 122)
        col.append(chr(random.randint(48, 57) if number < 48 else number))
    return ''.join(col)

def main(n, m):
    return [generator_password(m) for step in range(n)]

# print(*main(5,10))

# task 25.2 - Генератор паролей v.2
def generator_password_v2(length):
    if length < 3:
        return '- Выберите другую длину пароля!'
    alfavit = [[step for step in range(48, 58)], [step for step in range(65, 91)], [step for step in range(97, 123)]]
    col = [random.randint(0, 2) for l in range(length)]
    while not 0 in col or not 1 in col or not 2 in col:
        col = [random.randint(0, 2) for l in range(length)]
    for step in range(length):
        col[step] = random.randint(alfavit[col[step]][0], alfavit[col[step]][-1])
    return ''.join([chr(step) for step in col])

def main_v2(n, m):
    if m < 3:
        return '- Выберите другую длину пароля!'
    return [generator_password_v2(m) for step in range(n)]

# print(*main_v2(5,10), sep='\n')

# task 25.3 - ПИ
def pi():
    number = 0.0
    for step in range(500000):
        x = random.random() * ((step + 1) / (step + 1))
        y = random.random() * ((step + 1) / (step + 1))
        number += (x * x + y * y < 1.0)
    return 4 * number / 500000


# task 26.1 - Нарисуй градиент!
def draw_gradient(color):
    new_image = Image.new('RGB', (510, 200), (0, 0, 0))
    draw = ImageDraw.Draw(new_image)
    for i in range(0, 512, 2):
        rgb = tuple(int(i / 2) if step == 'rgb'.find(color) else 0 for step in range(3))
        draw.line((i, 0, i + 1, 200), fill=rgb, width=3)
    new_image.save('res.png', 'PNG')
# draw_gradient('b')

# task 26.2 - Шахматы
def board(num, size):
    new_image = Image.new('RGB', (num * size, num * size), (255, 255, 255))
    draw = ImageDraw.Draw(new_image)

    for k in range(0, num * size, size):
        for t in range(0, num * size, size):
            if (k + t) % (size * 2) == 0:
                draw.rectangle((k, t, k + size - 1, t + size - 1), fill=(0, 0, 0), width=0)
    new_image.save('res.png', 'PNG')
# board(8, 50)

# task 27.1 - Миниатюра для сайта
def make_preview(size, colors):
    im = Image.open('image.jpg')
    im = im.resize(size)
    im = im.quantize(colors)
    im.save('res.bmp')
# make_preview((300, 200), 64)

def negative(source):
    source = Image.open(source)
    result = Image.new('RGB', source.size)
    for k in range(source.size[0]):
        for t in range(source.size[1]):
            r, g, b = source.getpixel((k, t))
            result.putpixel((k, t), (255 - r, 255 - g, 255 - b))
    result.save('res.png', "PNG")
# negative('image.jpg')