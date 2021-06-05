# Шумская Екатерина Алексеевна

#1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
# переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
# состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
# — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
#Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
# соответствующее сообщение и завершать скрипт.


from time import sleep
from random import randint
colours = [['red', 7], ['yellow', 2], ['green', 5]]
len_c = len(colours) - 1
order_true = ['red', 'yellow', 'green']


class TrafficLight:
    def __init__(self):
        self.__colour = None
        
    def running(self):
        while True:
            order = []
            for _ in range(3):
                color = randint(0,len_c)
                self.__colour = colours[color][0]
                print(self.__colour)
                sleep(colours[color][1])
                order.append(colours[color][0])
            if order != order_true:
                print('Порядок переключения нарушен')
                break


tl1 = TrafficLight()
tl1.running()
