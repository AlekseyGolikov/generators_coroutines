# Программа иллюстрирует процесс создания собственного итератора на базе класса

from time import sleep
class IterClass:
    def __init__(self, max=0):
        self._max = max
    def __iter__(self):
        self._count = 0
        return self
    def __next__(self):
        if self._count < self._max:
            self._count += 1
            return self._count
        else:
            raise StopIteration

i = IterClass(5)
gen = iter(i)
try:
    while 1:
        c = next(gen)
        print(c)
        sleep(1)
except StopIteration:
    print('Счет окончен')