# Шумская Екатерина Алексеевна
"""Модуль удаляет позиции"""
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
    div_remove = input('Введите подразделение: ').upper()
    find = False
    for el in hw8.list_instance:    # Ищем с списке устройство с таким инвентарным номером
        if el.inv_number == inv_number_t and el.division == div_remove:        # Нашли на складе, добавим количество
            hw8.list_instance.remove(el)
            find = True
    if find:
        print('Объект удален')
    else:
        print('Объект не найден')

for el in hw8.list_instance:
    list_equipment.append([el.inv_number, el.division, el.name, el.count, el.param])
with open("hw8.json", "w") as file_j:
    json.dump(list_equipment, file_j)
