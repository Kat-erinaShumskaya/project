# Шумская Екатерина Алексеевна

# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите
# несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для
# классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
# свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
from random import randint

direction = [' повернула налево', ' повернула направо', ' едет прямо', ' развернулась']
color_list = ['red', 'orange', 'blue', 'dark blue', 'yellow']
name_car_list = ['Zhiguli', 'Audi', 'Lada', 'Lada Kalina', 'UAZ', 'Volga']
car_list = []       # В этот список соберем экземпляры классов


def status_cars():      # Применяет методы show_speed и turn ко всем экземплярам, выводит название и модель машины
    for i in range(len(car_list)):      # Выделим название класса машины
        class_name = str(car_list[i]).split(' ')
        class_name = class_name[0][10:]
        if car_list[i].is_police:
            is_police_str = 'Полицейская машина'
        else:
            is_police_str = ''
        if not car_list[i].speed == 0:
            print(f'Машина под номером {i+1}{car_list[i].turn(direction)} ({car_list[i].name} {car_list[i].color}'
                  f' класс {class_name}) {car_list[i].show_speed()} {is_police_str}')
        else:
            print(f'Машина под номером {i + 1} стоит ({car_list[i].name} {car_list[i].color}'
                  f' класс {class_name}) {is_police_str}')


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        car_list.append(self)

    def go(self):
        self.speed = randint(10, 120)

    def stop(self):
        self.speed = 0

    def turn(self, direct):
        return direct[randint(0, len(direct)-1)]

    def show_speed(self):
        return f'Текущая скорость {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            return f'Текущая скорость {self.speed} Превышение скорости!'
        else:
            return f'Текущая скорость {self.speed}'


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            return f'Текущая скорость {self.speed} Превышение скорости!'
        else:
            return f'Текущая скорость {self.speed}'


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

len_color = len(color_list) - 1
len_name = len(name_car_list) - 1
for _ in range(3):      # Создаем 15 экземпляров из разных классов
    Car(randint(10, 120), color_list[randint(0, len_color)], name_car_list[randint(0, len_name)], False)
    TownCar(randint(10, 120), color_list[randint(0, len_color)], name_car_list[randint(0, len_name)])
    SportCar(randint(10, 120), color_list[randint(0, len_color)], name_car_list[randint(0, len_name)])
    PoliceCar(randint(10, 120), color_list[randint(0, len_color)], name_car_list[randint(0, len_name)])
    WorkCar(randint(10, 120), color_list[randint(0, len_color)], name_car_list[randint(0, len_name)])

stop_car_number = [randint(0, len(car_list)-1) for i in range(6)]   # Сгенерируем номера машин, чтобы остановить
# print(stop_car_number)
for i in stop_car_number:
    car_list[i].stop()
status_cars()
for i in range(len(car_list)):      # Запустим все стоящие машины методом speed
    if car_list[i].speed == 0:
        car_list[i].go()
print('-------------------------------')
status_cars()

