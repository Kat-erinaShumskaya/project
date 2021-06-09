# Шумская Екатерина Алексеевна

# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
# Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.
matrix_list = []


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.ismatrix = True
        self.dim = []
        self.len_max = 1
        matrix_list.append(self)

    @property
    def dim(self):
        return self.__dim

    @dim.setter
    def dim(self, dim):     # Вычисляет размерность матрицы
        if type(self.matrix) == list:
            for i in range(len(self.matrix)):
                if type(self.matrix[i]) == list:
                    if len(self.matrix[0]) != len(self.matrix[i]) or type(self.matrix[0]) != type(self.matrix[i]):
                        self.__dim = []
                        self.ismatrix = False
                        break
                    else:
                        self.__dim = [len(self.matrix), len(self.matrix[0])]
                        self.ismatrix = True
                else:
                    if type(self.matrix[0]) != type(self.matrix[i]):
                        self.__dim = []
                        self.ismatrix = False
                        break
                    else:
                        self.__dim = [len(self.matrix)]
                        self.ismatrix = True
        else:
            self.ismatrix = False
            self.__dim = []

    @property
    def len_max(self):
        return self.__len_max

    @len_max.setter
    def len_max(self, len_max):  # Вычисляет максимальную длинну элементов в матрице
        if self.ismatrix:
            for el in self.matrix:
                if len(self.dim) == 1:
                    if len(str(el)) > len_max:
                        len_max = len(str(el))
                else:
                    for ell in el:
                        if len(str(ell)) > len_max:
                            len_max = len(str(ell))
        self.__len_max = len_max

    def __str__(self):
        if self.ismatrix:
            result = ''
            if len(self.dim) == 1:
                for i in range(self.dim[0]):
                    result = result + str(self.matrix[i]) + ' ' * (self.len_max + 3 - len(str(self.matrix[i])))
                result = '| ' + result + '|'
                return result
            else:
                for i in range(self.dim[0]):
                    r1 = ''
                    for j in range(self.dim[1]):
                        r1 = r1 + str(self.matrix[i][j]) + ' ' * (self.len_max + 3 - len(str(self.matrix[i][j])))
                    r1 = '| ' + r1 + '|\n'
                    result = result + r1
                return result
        else:
            return 'Объект не является матрицей'

    def __add__(self, other):
        if self.ismatrix:
            try:
                result = []
                for i in range(self.dim[0]):
                    result1 = []
                    if type(self.matrix[i]) == list:
                        for j in range(self.dim[1]):
                            result1.append(self.matrix[i][j] + other.matrix[i][j])
                    else:
                        result.append(self.matrix[i] + other.matrix[i])
                        continue
                    result.append(result1)
                return Matrix(result)
            except TypeError:
                return 'Нельзя складывать матрицы с разным типом данных'
        else:
            return 'Нельзя складывать не матрицы'


Matrix([1, 1, 1])   # 0
Matrix([2, 2, 2])   # 1
Matrix([[1, 2, 3], 1, [7, 8, 9]])   # 2
Matrix([[1, 1, 1], [1, 1, 1]])      # 3
Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 3000]])    #4
Matrix([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3], [4, 4, 4, 4]])   #5
Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])       # 6
Matrix([[3, 'a', 32], [2, '4', 6], [-1, 64, -8]])   # 7
Matrix([['a', 'b'], ['c', 'd']])    # 8
Matrix([[1], [1], [1]])  # 9
Matrix([[10], [12], [13]])  # 10
Matrix([1])     # 11
Matrix(1)       # 12
Matrix([[3, 'a', [1, 2]], [2, '4', 6], [-1, 64, -8]])   # 13
Matrix([[[3, 2], 'b', [3, 2]], [2, '4', 6], [-1, 0, -8]])
m = [[3, 'a', 32], [2, '4', 6], [-1, 64, -8]]
for el in matrix_list:
    print(el.matrix, el.ismatrix, el.dim, el.len_max)
    print(el)

print(matrix_list[0] + matrix_list[1])
print(matrix_list[2] + matrix_list[2])
print(2 + 2)
print(matrix_list[6] + matrix_list[7])
print(matrix_list[6] + matrix_list[4])
print(matrix_list[8] + matrix_list[8])
print(matrix_list[9] + matrix_list[10] + matrix_list[10])
print(matrix_list[11] + matrix_list[11])
print(matrix_list[13] + matrix_list[14])
