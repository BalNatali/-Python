import collections
pets = {
1:{
"Мухтар": {
"Вид питомца": "Собака",
"Возраст питомца": 9,
"Имя владельца": "Павел"
},
},
2:{
"Каа": {
"Вид питомца": "желторотый питон",
"Возраст питомца": 14,
"Имя владельца": "Саша"
},
},
}
def get_suffix(age):
    if age == 1:
        return "год"
    elif age > 1 and age < 5:
        return "года"
    else:
        return "лет"
def create(): #создавать новую запись с информацией о питомце и добавлять эту информацию в наш словарь pets
    print("### Комманда create")
    key = input("Кличка питомца: ")
    fields = ["Вид питомца", "Возраст питомца", "Имя владельца"]
    temp = {key: dict()}
    for field in fields:
        res = input(f"{field}: ")
        temp[key][field] = int(res) if res.isnumeric() else res
        last = collections.deque(pets, maxlen=1)[0]
        pets[last+1] = temp
def read():
    print("### Комманда read")
    ID = int(input("Введите ID: "))
    pet = get_pet(ID)
    if not pet:
        print(f"Нет питомца с таким ID:{ID}")
        return
    key = [x for x in pet.keys()][0]
    string = f'Это {pet[key]["Вид питомца"]} по кличке "{key}". ' \
f'Возраст питомца: {pet[key]["Возраст питомца"]} {get_suffix(pet[key]["Возраст питомца"])}. ' \
f'Имя владельца: {pet[key]["Имя владельца"]}'
    print(string)
def update(): #обновлять информацию об указанном питомце
    print("### Комманда update")
    ID = int(input("Введите ID: "))
    pet = get_pet(ID)
    if not pet:
        print(f"Нет питомца с таким ID:{ID}")
    else:
        kkey = [x for x in pet.keys()][0]
        print("Введите данные или оставьте поле пустым. Нажмите Enter")
        temp = dict()
        for key, value in pet[kkey].items():
            res = input(f"{key}: ")
            if res:
                temp[key] = int(res) if res.isnumeric() else res
                pet[kkey].update(temp)
            
def delete():
    print("### Комманда delete")
    ID = int(input("Введите ID: "))
    pets.pop(ID, None)
def get_pet(ID):
    return pets.get(ID, False)
def pets_list():
    for key, val in pets.items():
        print(f"ID:{key}", val)
commands = {
"create": create,
"read": read,
"update": update,
"delete": delete,
"list": pets_list,
"stop": 0
}
def spisok():
    print("Список доступных комманд:")
    for key in commands:
        print("- ", key)
    command = input('Введите команду: ')
    if command == "create":
        create()
        spisok()
    elif command == "read":
        read()
        spisok()
    elif command == "update":
        update()
        spisok()
    elif command == "delete":
        delete()
        spisok()
    elif command == "list":
        pets_list()
        spisok()
    elif command == "stop":
        print('Цикл завершён, спасибо!')
    else:
        print('Неверная команда, выберите из списка')
        spisok()
spisok()   
