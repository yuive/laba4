class Car:
    def __init__(self,name,color, is_police=False):
        self.name=name
        self.color=color
        self.is_police=is_police
        self.speed=0
    def go(self):
        print(f"{self.name}, поехала")
    def stop(self):
        print(f"{self.name}, остановилась")
    def turn(self,direction):
        print(f"{self.name}, повернула на {direction}")
    def show_speed(self):
        print(f"Текущая скорость{self.name}: {self.speed} км/ч ")

class TownCar(Car):
    def show_speed(self):
        if self.speed>60:
            print(f"{self.name}, превышает скорость")
        else:
            super().show_speed()
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"{self.name}, превышает скорость")
        else:
            super().show_speed()
class PoliceCar(Car):
    def __init__(self,name,color):
        super().__init__(name,color, is_police=True)

def choice_car():
    while True:
        print("Выберите тип автомобиля: ")
        print("1. TownCar ")
        print("2. SportCar ")
        print("3. WorkCar ")
        print("4. PoliceCar")
        сhoice = input("Введите чилсо (1-4): ")
        if сhoice in ('1','2','3','4'):
            return int(сhoice)
        else:
            print("Введено неверное число")

car_type=choice_car()
car_name=input("Введите название машины: ")
car_color=input("Введите цвет машины: ")

if car_type ==1:
    car=TownCar(car_name,car_color)
elif car_type ==2:
    car=SportCar(car_name,car_color)
elif car_type ==3:
    car=WorkCar(car_name,car_color)
elif car_type ==4:
    car=PoliceCar(car_name,car_color)

while True:
    command=input("Введите команду (go,stop,turn,show,exit): ")
    if command =='go':
        car.go()
        car.speed=int(input("Введите скорость: "))
    elif command=='stop':
        car.stop()
        car.speed=0
    elif command == 'turn':
        direction=input("Введите направление: ")
        car.turn(direction)
    elif command=='show':
        car.show_speed()
    elif command=='exit':
        break
    else:
        print("Неверно введена команда, повторите еще: ")
