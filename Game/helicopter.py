from utils import randcell
import os #библиотека, чистит консоль

class Helicopter:
    def __init__(self, w , h):
        rc = randcell (w, h)
        rx, ry = rc[0], rc[1]
        self.h = h
        self.w = w
        self.x = rx
        self.y = ry #начальное положение вертолёта
        self.tank = 0 #сколько у вертолёта воды (0 - нет воды, 1 - на один пожар, 2 - на два и так далее)
        self.mxtank = 1 #размер резервуара с водой (в магазине можно будет его увеличиь)
        self.score = 0 #счёт, за каждое успешно спасенное дерево даём 100 очков
        self.lives = 20 #жизни



    def  move (self, dx, dy):
        nx, ny = dx + self.x, dy + self.y
        if (nx >= 0 and ny >=0 and nx < self.h and ny < self.w):
            self.x, self.y = nx, ny

    def print_starts(self): #меню на которое будут выводиься количество воды, жизней, очки и т.д.
        print("🥛 ", self.tank, "/", self.mxtank, sep="", end=" | ") #сколько воды есть и максимум 
        print ("🏆", self.score, end= " | ") #сколько очков
        print("❤️ ", self.lives) #сколько жизней

    def game_over (self):
        os.system("cls") #это для Винды, для IOS и Linux надо писать os.system("clear")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X                                               X")
        print("X         GAME OVER, YOR SCORE IS", self.score, "         X")
        print("X                                               X")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        exit(0)    

    def export_data (self):
        return {"score": self.score,
                "lives": self. lives,
                "x": self.x, "y": self.y, 
                "tank": self.tank, "mxtank": self.mxtank}
        
    def import_data (self, data):
        self.x = data ["x"] or 0 #если в x data - null, то ставим 0
        self.y = data ["y"] or 0
        self.tank = data ["tank"] or 0
        self.mxtank = data ["mxtank"] or 1
        self.lives = data ["lives"] or 3
        self.score = data ["score"] or 0