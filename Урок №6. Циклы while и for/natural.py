x = int(input("Введите натуральное число до 2 млрд включительно: "))
a = 0
cnt = 0
while x <= 2e9 and x >= a:
    a += 1
    if x%a == 0:
        cnt += 1
print(cnt)
