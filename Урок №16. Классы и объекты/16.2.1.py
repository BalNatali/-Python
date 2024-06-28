class Turtle (object):
    x = 0
    y = 0
    s = 0
    def __init__ (self, x, y, s):
       self.x = x
       self.y = y
       self.s = s
    def go_up (self):
        self.y += self.s
    def go_down (self):
        self.y -= self.s
    def go_left (self):
        self.x -= self.s
    def go_right (self):
        self.y += self.s
    def evolve (self):
        self.s += 1
    def degrade (self):
        if self.s > 0:
            self.s -= 1
        else:
            raise ValueError('Невозможно уменьшить')
    def count_moves(self, x2, y2):
        return abs(x2- self.x) + abs(y2- self.y)
    
turtle_1 = Turtle (40, 40, 5)
turtle_1.go_up () #увеличивает y на s
print (turtle_1.x,turtle_1.y, turtle_1.s)
turtle_1.go_down () #уменьшает y на s
print (turtle_1.x,turtle_1.y, turtle_1.s)
turtle_1.go_left() #уменьшает x на s
print (turtle_1.x,turtle_1.y, turtle_1.s)
turtle_1.go_right() #увеличивает y на s
print (turtle_1.x,turtle_1.y, turtle_1.s)
turtle_1.evolve() #увеличивает s на 1
print (turtle_1.x,turtle_1.y, turtle_1.s)
turtle_1.degrade() #уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
print (turtle_1.x,turtle_1.y, turtle_1.s)
print (turtle_1.count_moves(10, 12)) #возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции