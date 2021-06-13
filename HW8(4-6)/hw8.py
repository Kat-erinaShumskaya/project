# Шумская Екатерина Алексеевна

# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# 5.Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую
# подходящую структуру, например словарь.
# 6.Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров,
# отправленных на склад, нельзя использовать строковый тип данных.

dict_type = {
    '1': 'printer',
    '2': 'scanner',
    '3': 'copier'
}
list_instance = []


class OfficeEquipment:
    def __init__(self, inv_number, division, name, count):
        self.inv_number = inv_number
        self.name = name
        self.division = division
        self.count = count
        list_instance.append(self)

    def transfer(self, count_t, div_in):
        if count_t > self.count:
            print('Перемещение невозможно')
        else:
            self.count = self.count - count_t
            # print(count_t)
            # print(self.count)
            find = False
            for el in list_instance:    # Ищем такой же объект в отделении, в которое перемещаем
                if el.inv_number == self.inv_number and el.division == div_in:
                    find = True
                    print('Такой объект существует, количество добавлено')
                    el.count = el.count + count_t
                    break
            if not find:
                if self.param == 'printer':
                    Printer(self.inv_number, div_in, self.name, count_t)
                elif self.param == 'scanner':
                    Scanner(self.inv_number, div_in, self.name, count_t)
                elif self.param == 'copier':
                    Copier(self.inv_number, div_in, self.name, count_t)
            if self.count == 0:
                list_instance.remove(self)


class Printer(OfficeEquipment):
    def __init__(self, inv_number, division, name, count):
        super().__init__(inv_number, division, name, count)
        self.param = 'printer'


class Scanner(OfficeEquipment):
    def __init__(self, inv_number, division, name, count):
        super().__init__(inv_number, division, name, count)
        self.param = 'scanner'


class Copier(OfficeEquipment):
    def __init__(self, inv_number, division, name, count):
        super().__init__(inv_number, division, name, count)
        self.param = 'copier'
