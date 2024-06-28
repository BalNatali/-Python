from map import Map #импортируем запуски карты и элементов
from pynput import keyboard #помогает взаимодействовать с кнопками на компьютере
from helicopter import Helicopter as Helico #вертолёт
from clouds import Clouds #облака
import time #библиотека, делает перерыв между выводами кадров
import os #библиотека, чистит консоль
import json #библиотека, из коробки превращает словари в json и наоборот


TICK_SLEEP = 0.05 #константа, сколько времени перерыв между кадрами
TREE_UPDATE = 50 # каждые 50 тиков (кадров) ставим дерево 
CLOUDS_UPDATE = 100 #как часто обновляюься облака
FIRE_UPDATE = 75 #каждые ... тиков убираем огни которые сгорели и зажигаем новые
MAP_W, MAP_H = 20, 10 #размеры карты

field = Map (MAP_W, MAP_H)
clouds = Clouds (MAP_W, MAP_H)
helico = Helico (MAP_W, MAP_H)
tick = 1 #создаём кадры (покадровое воиспроизведение игры) - динамика

MOVES = {'w':(-1, 0), 'd':(0, 1), 's':(1, 0), 'a':(0, -1)} #словарь из которого по ключу буквы будем возвращать перемещение по полю
# f - сохранение, g - восстановление сохраненного файла
def process_key (key): #код для взаимодействия с клавишами, key = зажатая клавиша
    global helico, tick, clouds, field #делаем объукт доступным в функции
    c = key.char.lower() #приводим введённыю букву (клавишу) к нижнему регистру и к символу
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)
    elif c == 'f':
        data = {"helicopter": helico.export_data(), 
                "clouds": clouds.export_data(), 
                "field": field.export_data(),
                "tick": tick}
        with open ("level.json", "w") as lvl: # открываем файл (только тут), если ставим r, то для чтения открываем, если w - для записи
            json.dump(data, lvl) #записываем файл. Передаём данные и куда записываем их
    elif c ==  'g':
        with open("level.json", "r") as lvl:
            data = json.load(lvl) #открываем на чтение
            tick = data["tick"] or 1
            helico.import_data (data ["helicopter"])
            field.import_data (data ["field"])
            clouds.import_data (data ["clouds"])


listener = keyboard.Listener( #код для взаимодействия с клавишами
    on_press = None,
    on_release = process_key,)
listener.start()





while True: #цикл будет работать всегда пока работает программа или пока мы не остановим его принудительно
    os.system("cls") #это для Винды, для IOS и Linux надо писать os.system("clear")
    field.process_helicopter(helico, clouds) #пополняем запасы воды по максимуму из реки (если вертолёт на клетке с рекой)
    helico.print_starts() # выводим меню с жизнями, запасами воды, очками и т.д. 
    field.print_map(helico, clouds) 
    print ("TICK", tick)    #каждый новый кадр выводим карту и номер тика (кадра) 
    tick += 1
    time.sleep(TICK_SLEEP) #передаём какой надо делать перевыв между кадрами в секунду
    if(tick % TREE_UPDATE == 0):
        field.generate_tree() #сажаем дерево в свободную клетку
    if (tick % FIRE_UPDATE == 0):
        field.update_fires()
    if (tick % CLOUDS_UPDATE == 0):
        clouds.update()