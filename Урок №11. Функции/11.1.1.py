def f(i): return 1 if i == 1 else i * f(i - 1)
n = int(input('Введите число: '))
x = (n-1)*n
spisok = [f(x - i) for i in range(x)]
print(spisok)