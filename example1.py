# тестовый документ

s = "hello 'world'"  # или escape последовательность 'dd \'fg', или 'dd "fg'
# \n переход на новую строку
print(s)

print('Примеры выводов')
value = None
a = 123
b = 1.23
print(a)
print(b)
value = 111
print(type(value))
print (a, '-', b, '-', s) 
print ('{1} - {2} - {0}'.format(a, b, s)) 
print (f'{a} - {b} - {s}') 

f = False 
print(f)

print('Примеры поиска в списке и проверки выражений: ')
list  = ['1', '2', '3']
print(list)
print(not 4 in list)

f = [1,2,3,4,5]
is_odd = not f[1] % 2 # нечётное - истина или другое is_odd = f[1] % 2 == 0 проверка на чётность, но можно без == 0
print(f)
print(is_odd)

print('Сумма чисел: ')
print('Введите k')
k = int(input())   #аналогично с float
print('Введите m')
m = int(input())
print(k, ' + ', m, ' = ', k+m)

print('Какое число больше: ')
a = int(input())
b = int(input())
if a>b:
    print(a)
else:
    print(b)


print('Переворот числа: ')
original = 12 # инвертирую, переворачиваю число
inverted = 0
print(original)
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Получившееся число')
print(inverted)

print('Возведение в степень каждого из последовательности (for): ')
for i in 1,2,3,4,5:  # возведение чисел в квадрат
    print(i**2)

r = range(6) # от 0 до 5 
print('И снова уже для: ')
for i in r:
    print(i)
print('Результат: ')
for i in r:
    print(i**2)

print('Пример использования функции: ')
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 15
    else:
        return

arg = 15
print(f(arg))