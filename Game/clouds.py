from utils import randbool #импортируем свой метод из файла utils.py

class Clouds:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]

    def update (self, r = 1, mxr = 20, g = 1, mxg = 10):
        for i in range (self.h):
            for j in range (self.w):
                if randbool(r, mxr):
                    self.cells[i][j] = 1 #ставим обычное обласко на рандомную ячейку
                    if randbool (g, mxg):
                        self.cells[i][j] = 2 #ставим грозовое облако
                else:
                    self.cells[i][j] = 0 #чистим облака

                
    def export_data (self):
        return {"cells": self.cells}
    
    def import_data (self, data):
        self.cells = data ["cells"] or [[0 for i in range(self.w)] for j in range(self.h)]