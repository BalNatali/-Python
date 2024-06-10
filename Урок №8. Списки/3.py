m = int(input('Максимальная масса, которую выдержит одна лодка: '))
n = int(input('Количество рыбаков: '))
a = []
b = []
for i in range(n):
    a.append(int(input()))
 
for x in range(len(a)):
    if a[x] + min(a) <= m:
        b += [[a[x], min(a)]]
        a[x] += m
        a[a.index(min(a))] += m
    else:
        if a[x] > m:
            continue
        else:
            b += [[a[x]]]
print("Всего нужно лодок:", len(b))