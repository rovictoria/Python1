# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.
# 1 –> Понедельник
# 10 –> Нет такого дня

print('1. По порядковому числу выдаёт день недели:')
def week_day(N):
    match N:
        case 1: print(f'{N} - Понедельник')
        case 2: print(f'{N} -  Вторник')
        case 3: print(f'{N} - Среда')
        case 4: print(f'{N} - Четверг')
        case 5: print(f'{N} - Пятница')
        case 6: print(f'{N} - Суббота')
        case 7: print(f'{N} - Воскресенье')
        case _: print('Нужно ввести число от 1 до 7, попробуйте снова :)')

number_of_day = int(input('Введите число, большее 1: '))
week_day(number_of_day)

# Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,09


# Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# 1 -> x > 0, y > 0

# Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
# 8 -> 2, 4, 6, 8
print('4. Все чётные от 1 до N')


def all_even_numbers(N):
    if N > 1:
        for i in range(1, N+1):
            if i % 2 == 0:
                print(i, end= ' ')
    else:
        print('Ваше число не подходит условию задачи, невозможно определить чётные числа [1,N]')

number = int(input('Введите число, большее 1: '))
all_even_numbers(number)