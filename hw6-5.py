# Шумская Екатерина Алексеевна

# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут
# title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом
# из классов реализовать переопределение метода draw. Для каждого из классов методы
# должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что
# выведет описанный метод для каждого экземпляра.
from random import randint
stationery_list = []


class Stationery:

    def __init__(self, title, width):
        self.title = title
        self.width = width
        stationery_list.append(self)

    def draw(self):
        print(f'Запуск отрисовки, толщина линии {self.width}')


class Pen(Stationery):

    def draw(self):
        print(f'Запуск отрисовки ручкой, толщина линии {self.width}')


class Pencil(Stationery):

    def draw(self):
        print(f'Запуск отрисовки карандашом, толщина линии {self.width}')


class Handle(Stationery):

    def draw(self):
        print(f'Запуск отрисовки маркером, толщина линии {self.width}')


for i in range(2):
    Stationery('неизвестная принадлежность', randint(1, 4))
    Pen('ручка', randint(1, 4))
    Pencil('карандаш', randint(1, 4))
    Handle('маркер', randint(1, 4))
for i in range(len(stationery_list)):
    stationery_list[i].draw()


