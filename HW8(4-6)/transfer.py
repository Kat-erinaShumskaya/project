# Шумская Екатерина Алексеевна
"""Модуль для перемещения объектов между подразделениями"""
import sys
import hw8
import json
import os
list_equipment = []
if os.path.exists('hw8.json'):
    with open("hw8.json", "r") as file_j:
        dict_data = json.load(file_j)
else:
    sys.exit('Нет данных')

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
    div_out = input('Введите подразделение, из которого объект перемещается: ').upper()
    count_t = input('Введите количество: ')
    find = False
    if count_t.isdigit() and count_t != '0':
        for el in hw8.list_instance:  # Ищем с списке устройство с таким инвентарным номером в указанном подразделении
            if el.inv_number == inv_number_t and el.division == div_out:  # Нашли
                find = True
                div_in = input('Введите подразделение, в которое объект перемещается: ').upper()
                el.transfer(int(count_t), div_in)
                continue
    else:
        print('Количество должно быть целым положительным числом')
    if not find:
        print(f'Объект с инвентарным номером {inv_number_t} в подразделении {div_out} не найден')

for el in hw8.list_instance:
    list_equipment.append([el.inv_number, el.division, el.name, el.count, el.param])
for el in hw8.list_instance:
    print(el.inv_number, el.division, el.name, el.count, el.param)
with open("hw8.json", "w") as file_j:
    json.dump(list_equipment, file_j)

