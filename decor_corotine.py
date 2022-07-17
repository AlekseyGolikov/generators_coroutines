"""
    Пример оборачивания инициализирующих методов сопрограммы в декоратор
"""
def coro(func):
    def wrapper():
        gen = func()
        next(gen)
        return gen
    return wrapper

@coro
def write_word():
    while True:
        word = (yield)
        if not word.isspace(): # Цикл прервется, если ввести пробел
            print(word)
        else:
            break

while True:
    write_word().send(input('Введите слово: '))