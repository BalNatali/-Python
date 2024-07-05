from utils import randbool #импортируем свой метод из файла utils.py
from utils import randcell #импортируем свой метод из файла utils.py
from utils import randcell2 #импортируем свой метод из файла utils.py



#0 - поле
#1 - дерево
#2 - река
#3 - госпиталь
#4 - магазин
#5 - огонь


CELL_TYPES= "🟩🌲🌊🏥🏪🔥" #каспом потому что объявление контанты, значения которое не поменяется

TREE_BONUS = 100 #сколько очков даём за потушенное дерево
UPGRADE_COST = 5000 #стоимость апгрейда резервуара для воды (+1)
LIFE_COST = 1000

class Map: #создаём карту. только то что на земле
    def __init__(self, w, h): #калькулятор создания карты с длиной и шириной
    #ряды h и w - клетки
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)]for j in range(h)]
        self.generate_forest(5, 10)
        self.generate_river(10)
        self.generate_river(10)
        self.generate_upgrade_shop()
        self.generate_hospital ()
        
    def check_bounds (self, x, y): #проверяет принадлежит ли клетка нашему полю, на вход получает x и y - координаты клетки
        #координата (0,0) находится в левой верхней клетке
        if ((x < 0) or (y < 0) or (x >= self.h) or (y >= self.w)):
            return False
        return True      

    def print_map (self, helico, clouds): #выводит карту
        print("⬛" * (self.w + 2))
        for ri in range (self.h): #row будет принимать значение списка cells, т.е. значение ряда
            print("⬛", end="")
            for ci in range (self.w): #проходим по клеткам с помощью cell
                cell = self.cells[ri][ci]
                if (clouds.cells [ri][ci] == 1):
                    print("⚪️", end = "")
                elif (clouds.cells [ri][ci] == 2):
                    print("☔️", end = "")
                elif (helico.x == ri and helico.y == ci):
                    print("🚁", end = "")
                elif (cell >= 0 and cell < len(CELL_TYPES)):  #что бы не выйти за границы строки (CELL_TYPES)
                    print(CELL_TYPES [cell], end="") # пишем end="" что бы не было переноса строки
            print("⬛")
        print("⬛" * (self.w + 2))            
#            print() #пустой print после каждого ряда для переноса строки     

    def generate_river (self, l): #генератор рек, ограничиваемся длиной реки (так же можно было бы сделать рандом)
        rc = randcell (self.w , self.h) #генерирует исток (откуда начнёт течь река)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while l > 0: #ставим новую клетку, пока не израсходуем всю длину реки
            rc2 = randcell2 (rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if (self.check_bounds(rx2, ry2)): #проверяем принадлежность клетки к полю
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l -= 1

    def generate_forest (self, r, mxr): #генератор лесов, пишем расширяемо, что бы можно было внести изменения
         #передаём вероятность с помощью 2 переменных: 1(mxr) - диапозон рандома, 2(r) - отсечка, отсекает все числа больше, чем наше число
        for ri in range (self.h):
            for ci in range (self.w):
                #используем нащ метод из файла utils.py
                if randbool (r, mxr):
                    self.cells[ri][ci] = 1 #ставим дерево

    def generate_tree(self): #генерируем рандомную клетку и если она не занята, то ставим туда дерево, если занята. то ничего не делаем
        c = randcell(self.w, self.h) #проверяем что клетка на поле
        cx, cy = c[0], c[1]
        if (self.cells [cx][cy] == 0): #проверяем что клетка свободна
            self.cells[cx][cy] = 1 # ставим дерево на пустую клетку

    def generate_upgrade_shop (self): #создаём магазин
        c = randcell (self.w, self.h) #берём рандомную клетку и ставим в неё магазин
        cx, cy = c[0], c[1]
        self.cells[cx][cy] = 4

    def generate_hospital (self): #создаём магазин
        c = randcell (self.w, self.h) #берём рандомную клетку и ставим в неё магазин
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] != 4: #если клетка не 4 (у нас не стоит там уже магазин, то ставим госпиталь, иначе ищем другое место)
            self.cells[cx][cy] = 3
        else:
            self.generate_hospital()

    def add_fire(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1] #генерируем рандомную клетку
        if self.cells [cx][cy] == 1: #проверяем что на клетке уже есть дерево 
            self.cells[cx][cy] = 5 #ставим огонь

    def update_fires (self, helico):
        for ri in range (self.h):
            for ci in range (self.w):
                cell = self.cells[ri][ci]
                if cell == 5:
                    self.cells[ri][ci] = 0 #вместо огня ставим пустое поле, так как дерево уже сгорело
                    helico.score -= TREE_BONUS
        for i in range (10):
            self.add_fire()

    def process_helicopter (self, helico, clouds): #заполняем резервуар с водой из реки
        c = self.cells[helico.x][helico.y]
        d = clouds.cells[helico.x][helico.y]
        if (c == 2):
            helico.tank = helico.mxtank #пополняем резервуар от реки по максимуму
        if (c == 5 and helico.tank > 0): #тушим пожар, если он есть
            helico.tank -= 1
            helico.score += TREE_BONUS #даём очки за спасение дерева
            self.cells[helico.x][helico.y] = 1
        if (c==4 and helico.score >= UPGRADE_COST):
            helico.mxtank += 1
            helico.score -= UPGRADE_COST
        if (c==3 and helico.score >= LIFE_COST):
            helico.lives += 10
            helico.score -= LIFE_COST
        if (d == 2):
            helico.lives -= 1
            if (helico.lives == 0): #игра окончена, проигрыш
                helico.game_over()

    def export_data (self):
        return {"cells": self.cells}
    
    def import_data (self, data):
        self.cells = data ["cells"] or [[0 for i in range(self.w)] for j in range(self.h)]