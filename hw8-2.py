# Шумская Екатерина Алексеевна

# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
# в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


number1 = input("Введите делимое: ")
number2 = input("Введите делитель: ")
try:
    number1 = float(number1)
    number2 = float(number2)
    if number2 == 0:
        raise MyError("Нельзя делить на ноль")
except (ValueError, MyError) as err:
    print(err)
else:
    print(f"Результат: {number1 / number2}")
