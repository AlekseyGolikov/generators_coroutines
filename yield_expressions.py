# Пример реалзиации yield выражения
#         Вывод:
#         Готов к приему значний:
#         ведите значение: str1
#         Получено значение: str1
#         ведите значение: str2
#         Получено значение: str2
#         ведите значение: str3
#         Получено значение: str3
#         ведите значение:

def receiver():
    print('Готов к приему значний:')
    while 1:
        n = (yield)
        print('Получено значение: %s' % n)

r = receiver()
r.__next__()
while True:
    try:
        r.send(input('ведите значение: '))
    except KeyboardInterrupt:
        print('Передача окончена!')
        break
