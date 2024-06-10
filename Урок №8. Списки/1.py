n = int(input('Введите количество чисел в массиве: '))
if ( n >= 1) and (n <= 100000):
    print(*[int(input()) for _ in range(n)][::-1])
