# Шумская Екатерина Алексеевна

# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное
# название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды
# существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size == 0:
            self.__size = 0
        elif size < 42:
            self.__size = 42
        elif size > 60:
            self.__size = 60
        else:
            if size % 2 == 1:
                self.__size = size + 1
            else:
                self.__size = size

    def fabric_consumption(self):
        # (V/6.5 + 0.5)
        if self.size == 0:
            return 0
        else:
            return round(self.size / 6.5 + 0.5, 2)


class Jacket(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height == 0:
            self.__height = 0
        elif height < 150:
            self.__height = 150
        elif height > 210:
            self.__height = 210
        else:
            self.__height = height

    def fabric_consumption(self):
        # (2 * H + 0.3)
        if self.height == 0:
            return 0
        else:
            return round((self.height / 100) * 2 + 0.3, 2)


def coats_fabric_consumption(list):
    coats_fabric_consumption = []
    for el in list:
        coats_fabric_consumption.append(Coat(el).fabric_consumption())
    return sum(coats_fabric_consumption)


def jackets_fabric_consumption(list):
    jackets_fabric_consumption = []
    for el in list:
        jackets_fabric_consumption.append(Jacket(el).fabric_consumption())
    return sum(jackets_fabric_consumption)


try:
    list1 = list(map(int, input('Введите через пробел размеры для пальто: ').split(' ')))
    list2 = list(map(int, input('Введите через пробел рост в см для жакетов: ').split(' ')))
    print(f'На все изделия потребуется {coats_fabric_consumption(list1) + jackets_fabric_consumption(list2)}м ткани')
except ValueError:
    print('Вы ввели некорректные данные')

for i in [42, 38, 55]:
    print(f'i = {i}, размер равен {Coat(i).size}, расход ткани {Coat(i).fabric_consumption()}м')
for i in [140, 168, 211]:
    print(f'i = {i}, рост равен {Jacket(i).height}, расход ткани {Jacket(i).fabric_consumption()}м')

