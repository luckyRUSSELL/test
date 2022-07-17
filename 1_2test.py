import cProfile
from random import randrange

def bin(mas):
    new_mas = sorted(mas)
    return new_mas



a = [randrange(1,100) for i in range(100)]
print(bin(a))
cProfile.run('bin(mas)')


"""В большинстве случаях,используется встроенный метод сортировки,
быстрая сортировка является одной из самых быстрых и по времени она 
выполняется примерно столько же,сколько и встроенная
"""