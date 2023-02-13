# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.

# 2 2
# 4

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

def sum(a, b):
    if (b == 1): return a + 1
    elif (b == 0): return a
    else:
        a += sum(1, b-1)
        return a

print(sum(a, b))