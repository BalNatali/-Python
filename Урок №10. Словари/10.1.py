pets ={}
pets2={}
while (True):
    k=input("Введите имя питомца: ")
    if k=='':
        break
    else:
        k1=input('Вид питомца: ')
        k2=int(input('Возраст питомца: '))
        break
year_case = ''
if k2 % 10 == 1 and k2 != 11 and k2 % 100 != 11:
    year_case = 'год'
elif 1 < k2 % 10 <= 4 and k2 != 12 and k2 != 13 and k2 != 14:
    year_case = 'года'
else:
    year_case = 'лет'
k3=input('Имя владельца:  ')
pets2={'Вид питомца:':k1, 'Возраст питомца:':k2, 'Имя владельца:':k3  }
pets[k]=pets2
for key in pets.keys():
    print("Это", pets2['Вид питомца:'], "по кличке", key,". Возраст питомца:", pets2['Возраст питомца:'], year_case,".", "Имя владельца:", pets2['Имя владельца:'],".")