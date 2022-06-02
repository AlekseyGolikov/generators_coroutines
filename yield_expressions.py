# Пример реалзиации yield выражения
#         Вывод:
#         Готов к приему значений
#         Введите значение: 323
#         Получено 323
#         Введите значение: we
#         Получено we
#         Введите значение: exit
#         Получено exit
#         Передача закончена!
#
#         Process finished with exit code 0

def coroutine(func):
    def wrapper(*args):
        g = func(*args)
        g.__next__()
        return g
    return wrapper

@coroutine
def receiver():
    print('Готов к приему значений')
    while True:
        str = (yield)
        print('Получено %s' % str)
        if str == 'exit':
            raise GeneratorExit


r = receiver()
while 1:
    try:
        r.send(input('Введите значение: '))
    except GeneratorExit:
        break
print('Передача закончена!')
