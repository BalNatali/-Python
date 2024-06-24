class Cassa (object):
    money = 0
    def __init__ (self,m):
        self.money = m

    def top_up (self, x):
        self.money += x
    def count_1000 (self):
        s = self.money // 1000
        return s
    def take_away (self, x):
        if x <= self.money:
            self.money -= x
        else:
            raise ValueError('Not enough money')
cassa_1 = Cassa(10) #начальная сумма в кассе
cassa_1.top_up (3000) #пополнение кассы
print(cassa_1.count_1000()) #сколько целых 1 000 осталось в кассе
cassa_1.take_away(6000)   # Попытка снять 6000 из кассы 
