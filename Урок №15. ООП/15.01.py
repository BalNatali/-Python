class Transport:
    
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
class Autobus (Transport):
    
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)
        
    def __str__(self):
        return "Название автомобиля: "+self.name+" Скорость: "+str(self.max_speed)+" Пробег: "+str(self.mileage)
        
Autobus = Autobus ('Renault Logan', 180, 12)
print(Autobus)