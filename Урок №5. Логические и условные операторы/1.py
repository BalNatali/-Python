print("Введите любое число")
a=int(input())
if (a > 0) and (a%2 == 0):
    print("положительное чётное число")
elif (a > 0) and (a%2 > 0):
    print("положительное нечётное число")
elif (a < 0) and (a%2 == 0):
    print("отрицательное чётное число")
elif a == 0:
    print("нулевое число")
else:
    print("отрицательное нечётное число")
