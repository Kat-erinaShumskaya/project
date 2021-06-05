# Шумская Екатерина Алексеевна

# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен
# быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
# на базе класса Worker. В классе Position реализовать методы получения полного
# имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).
workers = []


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
        workers.append(self)


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


Position('Илья', 'Разумовский', 'Руководитель', 5000, 2000)
Position('Сергей', 'Молчанов', 'Слесарь', 3000, 1000)
Position('Варвара', 'Ильинична', 'Бухгалтер', 15000, 12000)
for i in range(len(workers)):
    print(str(workers[i].__dict__.values()))
    print(f'{workers[i].get_full_name()}, доход {workers[i].get_total_income()}')
