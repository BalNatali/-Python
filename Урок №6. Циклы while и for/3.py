a = int(input('Введите любое целое число: '))
b = int(input('Введите любое целое число: '))
if a <= b:
    for i in range (a, b):
        if i%2 == 0:
            print(i, end=" ", sep=" ")
