# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(n):
    fib_lst = [0]
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
        fib_lst.append(x)
        fib_lst.insert(0, -x if i % 2 else x)
    return fib_lst
fib_num = int(input("Введите число: "))
print(f"для к= {fib_num} список будет выглядеть так: {fib(fib_num)}")