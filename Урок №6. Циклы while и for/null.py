n = int(input())
x = 0
cnt = 0
while x < n:
    a = int(input('Введите любое целое число: '))
    x += 1
    if a == 0:
        cnt +=1
print("Количество целых чисел равных нулю:",cnt)