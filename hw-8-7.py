# Шумская Екатерина Алексеевна

# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
# перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры
# класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность
# полученного результата.

class ComplexNumber:
    def __init__(self, real_part, complex_part):
        self.real_part = real_part
        self.complex_part = complex_part

    def __add__(self, other):
        return ComplexNumber(self.real_part + other.real_part, self.complex_part + other.complex_part)

    def __mul__(self, other):
        real_p = self.real_part * other.real_part - self.complex_part * other.complex_part
        complex_p = self.real_part * other.complex_part + self.complex_part * other.real_part

        return ComplexNumber(real_p, complex_p)

    def __str__(self):
        return f'{self.real_part} + {self.complex_part}j'


a = ComplexNumber(5, 7)
b = ComplexNumber(1, 2)
d = ComplexNumber(1, 1)
e = ComplexNumber(-59, 2.23)

print(a + a + b + a + e)
print(a * b * e)
print(d * d * e)
