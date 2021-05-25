# Шумская Екатерина Алексеевна

def is_number(str):    # Функция, проверяющая, можно ли str конвертировать во float
    try:
        float(str)
        return True
    except ValueError:
        return False

# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.


def divide(arg1, arg2):
    try:
        arg3 = arg1 / arg2
        return arg3
    except ZeroDivisionError:
        print('Делить на ноль нельзя')


a = input('Введите делимое: ')
b = input('Введите делитель: ')
if is_number(a) and is_number(b):
    a = float(a)
    b = float(b)
    c = divide(a, b)
    if c != None:
        print(f'{a} / {b} = {round(c, 2)}')
else:
    print('Вы ввели некоректные данные')


# 2. Реализовать функцию, принимающую несколько параметров, описывающих
# данные пользователя: имя, фамилия, год рождения, город проживания, email,
# телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_func(na, ye, em, ph, su, ci):
    print(f'Имя - {na}, Фамилия - {su}, год - {ye}, город проживания - {ci}, email - {em}, телефон - {ph}')


name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Введите электронный адрес: ')
phone = input('Введите телефон: ')
my_func(na=name, su=surname, ye=year, ci=city, em=email, ph=phone)


# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func_sum(arg1, arg2, arg3):
    a = [arg1, arg2, arg3]
    a.sort()
    if a[0] == a[1]:
        return None
    else:
        return a[1] + a[2]


num1 = input('Введите первое число: ')
num2 = input('Введите второе число: ')
num3 = input('Введите третье число: ')
if is_number(num1) and is_number(num2) and is_number(num3):
    num1 = float(num1)
    num2 = float(num2)
    num3 = float(num3)
    if my_func_sum(num1, num2, num3) != None:
        print(my_func_sum(num1, num2, num3))
    else:
        print('Нет двух наибольших чисел')
else:
    print('Вы ввели некоректные данные')


# 4. Программа принимает действительное положительное число x и целое отрицательное
# число y. Необходимо выполнить возведение числа x в степень y. Задание необходимо
# реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись
# без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень
# с помощью оператора **. Второй — более сложная реализация без оператора **,
# предусматривающая использование цикла.


def my_func_pov(x, y):
    result = 1
    for i in range(0, abs(y)):
        result = result / x
    return result


def my_func_pov1(x, y):
    return x ** y


num_pov_1 = input('Введите первое число: ')
num_pov_2 = input('Введите второе число: ')
if is_number(num_pov_1) and is_number(num_pov_2):
    num_pov_1 = float(num_pov_1)
    num_pov_2 = int(num_pov_2)
    if num_pov_2 < 0:
        print(my_func_pov(num_pov_1, num_pov_2))
        print(my_func_pov1(num_pov_1, num_pov_2))
    else:
        print('Второе число должно быть отрицательным')
else:
    print('Вы ввели некоректные данные')


# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
# ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел
# будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный
# символ, выполнение программы завершается. Если специальный символ введен после нескольких
# чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого
# завершить программу.

result = 0
check_out = False
while check_out == False:
    numbers = input('Введите числа, которые нужно сложить, через пробел, для выхода введите q: ')
    num_list = numbers.split(' ')
    for i in range(len(num_list)):
        if num_list[i] == 'q':
            check_out = True
            break
        elif is_number(num_list[i]):
            num_list[i] = float(num_list[i])
            result = result + num_list[i]
        else:
            continue
    print(result)


# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
# возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.


def my_func_title_en(a):
    a = list(a)
    for i in range(len(a)):     # все буквы делаем строчными, вдруг все же есть заглавные не на 1 месте.
        if 65 <= ord(a[i]) <= 90:
            a[i] = chr(ord(a[i]) + 32)
    for i in range(len(a)):     # первую букву делаем заглавной, в цикле, т.к. в начале м.б. цифры и знаки
        if 97 <= ord(a[i]) <= 122:
            a[i] = chr(ord(a[i]) - 32)
            return ''.join(a)
        else:
            i += 1
    return ''.join(a)


def my_func_title(a):       # Та же, что и my_func_title_en(a), но и для русских букв
    a = list(a)
    for i in range(len(a)):     # все буквы делаем строчными, вдруг все же есть заглавные не на 1 месте.
        if (65 <= ord(a[i]) <= 90) or (1040 <= ord(a[i]) <= 1071):
            a[i] = chr(ord(a[i]) + 32)
    for i in range(len(a)):     # первую букву делаем заглавной
        if (97 <= ord(a[i]) <= 122) or (1072 <= ord(a[i]) <= 1103):
            a[i] = chr(ord(a[i]) - 32)
            return ''.join(a)
        else:
            i +=1
    return ''.join(a)


# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных
# пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной
# строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную
# ранее функцию int_func().

my_string = input('Введите строку: ')
print(my_string.title())        # Для проверки запустим метод .title()
my_list = my_string.split(' ')
for i in range(len(my_list)):
    my_list[i] = my_func_title(my_list[i])
print(' '.join(my_list))
