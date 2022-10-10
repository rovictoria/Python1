# Напишите программу, которая на вход 
# принимает число и выдаёт его квадрат (число 
# умноженное на само себя).

# def square(a):
#     return a**2

# number = 5
# print('Дано', number)
# print('Его квадрат', square(number))
print('1. Вычислить квадрат числа: ')
number = int(input('Введите число: '))
print(f'{number} * {number} = {number**2}')

# На вход принимает два числа и проверяет,
# является ли одно число квадратом другого.
print('2. Является ли одно число квадратом другого?')

number1 = int(input('Введите число: '))
number2 = int(input('Введите число: '))

print(number2**2 == abs(number1) or number1**2 == abs(number2))

# Организуйте последовательный ввод чисел до тех
# пор, пока не будет введён 0. Подсчитайте среди введённых чисел те,
# которые кратны трём.

element = None
count = 0

while element != 0:
    element = int(input('Введите число последовательности:'))
    if  element % 3 == 0 and element != 0:
        count += 1
    
print('Ввод окончен')
print('Количество чисел, кратных 3: ', count)

# Напишите программу, которая будет на вход
# принимать число N и выводить числа от -N до N
print('Вывод чисел от -N до N')
N = int(input('Введите число: '))
result = range(-N, N+1)
print(*result)

print('Или так: ')
for i in result:
    print(i)
    # если так, будет с переносом, если в строку, то надо print(i, end= '') пробел вместо перехода


# Дано трёхзначное число N. Определить кратна ли трём сумма всех его цифр.

# Дано трёхзначное число N. Определить, есть ли среди его цифр 4 или 7.

# Дан массив длиной 10 элементов. Заполнить его последовательно числами от 1 до 10.

# Задача 2. Напишите метод, который заполняет массив случайным количеством (от 1 до 100)
# нулей и единиц. Размер массива должен совпадать с квадратом количества единиц в нём.

# Напишите программу, которая будет на вход
# принимать число N и выводить числа от -N до N
# 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# Задача 1. Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число. Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.

# {0, 5, 6, 2, 7, 7, 8, 1, 1, 9} - 277 -> да
# {4, 4, 3, 6, 7, 0, 8, 5, 1, 2} - 812 -> нет