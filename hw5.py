# Шумская Екатерина Алексеевна

# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

with open("hw5-1out.txt", "a", encoding="utf-8") as file1out:
    while True:
        str_temp1 = input('Введите строку: ')
        if len(str_temp1) == 0:
            break
        else:
            print(str_temp1, file=file1out)

# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.

''' Функция ending вычисляет окончание для слова "слов " '''


def ending(my_list):
    s = str(len(my_list))
    if len(s) > 1:
        if s[-2] == '1':
            eleven = True
        else:
            eleven = False
    else:
        eleven = False
    if s[-1] == '1' and not eleven:
        return 'о'
    elif s[-1] in ['2', '3', '4'] and not eleven:
        return 'а'
    else:
        return ''


with open("hw5-2.txt", "r", encoding="utf-8") as file2:
    file2.seek(0)
    i = 0
    for li in file2:
        print(f"{i+1} строка содержит {len(li.split(' '))} слов{ending(li.split(' '))}")
        i += 1
    print(f'Строк: {i}')


# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open("hw5-3.txt", "r", encoding="utf-8") as file3:
    text3 = file3.read()
    file3.seek(0)
    list3 = []
    for li in file3:
        list_temp = li.split(' ')
        if '\n' in list_temp[1]:
            list_temp[1] = list_temp[1][0:-1]
        try:
            list_temp[1] = float(list_temp[1])
            list3.append(list_temp)
        except ValueError:
            print(f'Нарушена структура данных в строке {list_temp}, в расчет среднего дохода она не включена')

    for i in range(len(list3)):
        if list3[i][1] < 20000:
            print(list3[i][0])
    print('имеют оклад меньше 20000 руб.')
    sum_salary = 0
    for i in range(len(list3)):
        sum_salary += list3[i][1]
    print(f'Средняя величина дохода сотрудников составляет {round(sum_salary / len(list3), 2)} руб.')


# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны заменяться на
# русские. Новый блок строк должен записываться в новый текстовый файл.

dict4 = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}
with open("hw5-4.txt", "r", encoding="utf-8") as file4:
    text4 = file4.read()
    file4.seek(0)
    for li in file4:
        list_temp4 = li.split(' ')
        list_temp4[0] = dict4[list_temp4[0]]
        str_temp4 = ' '.join(list_temp4)
        with open("hw5-4out.txt", "a", encoding="utf-8") as file4out:
            file4out.write(str_temp4)


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import random
with open("hw5-5out.txt", "a", encoding="utf-8") as file5out:
    i = 0
    while i < 10:
        file5out.write(str(round(random()*100, 2)) + ' ')
        i += 1
with open("hw5-5out.txt", "r", encoding="utf-8") as file5:
    text5 = file5.read()
    file5.seek(0)
    list5 = text5[:-1].split(' ')
    for i in range(len(list5)):
        list5[i] = float(list5[i])
    print(round(sum(list5), 2))
