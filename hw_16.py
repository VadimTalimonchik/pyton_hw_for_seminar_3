# Задача 16.
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai . Последняя строка содержит число X.
# 5
# 1 2 3 4 5
# 3
# -> 1

n = int(input('Введите количество элементов в массиве: '))
print()

list_1 = list()
for i in range(n):
    ai = int(input('Введите число: '))
    list_1.append(ai)
print()

x = int(input('Введите искомое число в массиве: '))
print()

print('Число', x, 'встречается в массиве', list_1.count(x), 'раз(а).')
print()