# Шумская Екатерина Алексеевна

# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def get_numbers(cls, data):
        data_list = data.split('-')
        return list(map(int, data_list))

    @staticmethod
    def validation(data):
        try:
            data_list = Data.get_numbers(data)
            if not ((0 < data_list[0] < 32) or (0 < data_list[1] < 13) or (1990 < data_list[2] < 2101)):
                raise MyError('Ошибка ввода данных')
        except (MyError, ValueError) as err:
            print(err)
        else:
            print(data_list)


Data.validation(input('Введите дату в формате день-месяц-год: '))
