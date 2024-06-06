word = input('Введите слово без пробелов: ')
a = word.lower() [ : :1]
b = word.lower() [ : :-1]
if a == b:
    print('yes')
else:
    print('no')