# Шумская Екатерина Алексеевна
"""Модуль добавляет новые позиции всегда на склад"""
import hw8
import json
import os
list_equipment = []


def input_inst(inv_number_i, name_i, count_i, type_inst):
    if type_inst == 'printer':
        hw8.Printer(inv_number_i, 'СКЛАД', name_i, count_i)
    elif type_inst == 'scanner':
        hw8.Scanner(inv_number_i, 'СКЛАД', name_i, count_i)
    elif type_inst == 'copier':
        hw8.Copier(inv_number_i, 'СКЛАД', name_i, count_i,)


if os.path.exists('hw8.json'):
    with open("hw8.json", "r") as file_j:
        dict_data = json.load(file_j)
    for i in range(len(dict_data)):
        if dict_data[i][4] == 'printer':
            hw8.Printer(dict_data[i][0], dict_data[i][1], dict_data[i][2], dict_data[i][3])
        elif dict_data[i][4] == 'scanner':
            hw8.Scanner(dict_data[i][0], dict_data[i][1], dict_data[i][2], dict_data[i][3])
        elif dict_data[i][4] == 'copier':
            hw8.Copier(dict_data[i][0], dict_data[i][1], dict_data[i][2], dict_data[i][3])
    for el in hw8.list_instance:
        print(el.inv_number, el.division, el.name, el.count, el.param)

while True:
    inv_number_t = input('Введите инвентарный номер, для выхода введите q: ').upper()
    if inv_number_t == 'Q':
        break
    count_t = input('Введите количество: ')
    if count_t.isdigit() and count_t != '0':
        find = False
        find_sk = False
        for el in hw8.list_instance:    # Ищем с списке устройство с таким инвентарным номером
            # print(el.inv_number, el.division)
            if el.inv_number == inv_number_t and el.division == 'СКЛАД':        # Нашли на складе, добавим количество
                el.count = el.count + int(count_t)
                print('Объект с таким номером найден на складе, количество добавлено')
                find_sk = True
                continue
            elif el.inv_number == inv_number_t and el.division != 'СКЛАД':  # Нашли не на складе, скопируем параметры
                type_eq = el.param
                name_equipment = el.name
                find = True
                continue
        if find and not find_sk:    # Если нашли не на складе
            print(f'Объект с таким инвентарным номером найден {type_eq}, {name_equipment} ')
            input_inst(inv_number_t, name_equipment, int(count_t), type_eq)
        elif not (find or find_sk):    # Если нигде не нашли
            type_eq_key = input(f'Выберите тип устройства: 1 - принтер, 2 - сканер, 3 - копировальный аппарат: ')
            if type_eq_key in ['1', '2', '3']:
                name_equipment = input('Введите название устройства: ').upper()
                input_inst(inv_number_t, name_equipment, int(count_t), hw8.dict_type[type_eq_key])
            else:
                print('Неверно выбран тип устройства')
        else:
            continue
    else:
        print('Количество должно быть целым положительным числом')

for el in hw8.list_instance:
    list_equipment.append([el.inv_number, el.division, el.name, el.count, el.param])
with open("hw8.json", "w") as file_j:
    json.dump(list_equipment, file_j)
