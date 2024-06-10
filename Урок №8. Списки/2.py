def rot(arr): return arr[-1:] + arr[:-1]
n= int(input('Введите количество чисел в массиве: '))
if ( n >= 1) and (n <= 100000):
    print(*rot(input().split()))