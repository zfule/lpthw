class Car(object):
    price = 100000
    def __init__(self, c):
        self.color = c


car1 = Car("Red")
car2 = Car("Blue")
print(car1.color, Car.price)

Car.price = 110000
Car.name = 'QQ'
car1.color = 'Yellow'
print(car2.color, Car.price, Car.name)
print(car1.color, Car.price, Car.name)


import types
def setSpeed(self, s):
    self.speed = s


car1.setSpeed = types.MethodType(setSpeed, car1)
car1.setSpeed(50)
print(car1.speed)
