import random
#устанавливаем размер матрицы
a = int(input('a = '))
b = int(input('b = '))
#заполняем матрицу 1 рандомными числами
matrix_1=[[random.randint(1, 11) for j in range(b)] for i in range(a) ]
print('Matrix 1: ')
for i in range(a):
    print(matrix_1[i])
#заполняем матрицу 2 рандомными числами
matrix_2 = [ [ random.randint(1, 11) for j in range(b)] for i in range(a) ]
print('Matrix 2: ')
for i in range(a):
    print(matrix_2[i])
#складываем матрицы
result = [[matrix_1[i][j] + matrix_2[i][j]  for j in range
(len(matrix_1[0]))] for i in range(len(matrix_1))]
print("Результат сложения двух матриц: ")
for r in result:
    print(r)