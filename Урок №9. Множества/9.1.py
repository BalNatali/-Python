n = int(input('Введите количество элементов списка: '))
if n <= 100000 and n >= 1:
    spisok = list(map(int, input().split()))[:n]
    e=set(spisok)
    print(len(e))