# Программа перебирает генератором целые числа
# и записывает поочередно в файл out.txt

from time import sleep

def generator():
    """Генератор, который генерирует последовательность"""
    n = 0
    while n < 10:
        yield n
        n += 1

def coroutine():
    try:
        while True:
            n = (yield)
            with open('out.txt', 'a') as f:
                f.write('%s, ' % n)
    except GeneratorExit:
        pass

def copy():
    g = generator()
    c = coroutine()
    c.__next__()
    while 1:
        try:
            n = g.__next__()
            c.send(n)
            print(n)
            sleep(1)
        except StopIteration:
            print('Запись окончена!')
            break

if __name__ == '__main__':
    # c = coroutine()
    # c.__next__()
    # for i in range(5):
    #     print(i)
    #     c.send(i)
    #     sleep(1)
    copy()
