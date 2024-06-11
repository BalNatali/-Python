a = int(input('Введите количества чисел первого списка: '))
al = []
for i in range (a):
    number = input('Введите число: ')
    al.append (number)
mn1 = set(al)
b = int(input('Введите количества чисел второго списка:: '))
bl = []
for i in range (b):
    number = input('Введите число: ')
    bl.append (number)
mn2 = set(bl)
print(len(mn1.intersection(mn2)))