# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list = list(map(int, input("Введите числа через пробел: ").split()))
sum = 0
for i in range(len(list)):
    if i % 2 != 0:
        sum += list[i]
print(list)
print(f"Сумма равна: {sum}")


