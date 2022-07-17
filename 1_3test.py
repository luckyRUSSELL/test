# q = []
#
# q.append(1)
# q.append(2)
# q.append(3)
#
# print(q.pop(0))
# print(q.pop(1))

"""Используем простой список,но по времени не очень эффективно,потому что после удаления
идёт сдвиг в списке ,что занимает 0(n) времени"""


from collections import deque

q = deque()

q.append(1)
q.append(2)
q.append(3)

print(q)
print(q.popleft())
print(q.popleft())
print(q.popleft())


"""Класс deque- это отличный выход,в стандартной библиотеке,у него неплохая производительность(для
входящих и выходящих элементов"""