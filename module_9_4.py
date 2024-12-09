first = 'Мама мыла раму'
second = 'Рамена мало было'

# Lambda функция:
print(list(map(lambda x, y: x == y, first, second)))

# Замыкание:
def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for data in data_set:
                file.write(str(data) + '\n')
    return write_everything

write = get_advanced_writer('Example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке' ])

# метод __call__:
from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        word = choice(self.words)
        return word

first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Вероятно', 'Невозможно')
print(first_ball())
print(first_ball())
print(first_ball())
