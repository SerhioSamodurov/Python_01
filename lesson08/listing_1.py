"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""

class Matrix:

    def __init__(self, matrix_1):
        self.matrix_1 = matrix_1
        self.result = [[None, None, None],  [None, None, None]]

    def __add__(self, other):
        for i in range(len(self.matrix_1)):
            for l in range(len(other.matrix_1[i])):
                self.result[i][l] = self.matrix_1[i][l] + other.matrix_1[i][l]
        return self.result

    def __str__(self):
        return f'Объект класса Matrix - {self.matrix_1}'


mtrx =  Matrix([[1, 2, 3], [4, 5, 6]])
print(mtrx)
mtrx2 = Matrix([[1, 2, 3], [4, 5, 6]])
print(mtrx2)
m = mtrx + mtrx2
print(m)




# x = [[1, 2, 3], [4, 5, 6]]
# y = [[1, 2, 3], [4, 5, 6]]
#
#
# total = [[None, None, None], [None, None, None]]
#
# for i in range(len(x)):
#     for l in range(len(y[i])):
#         total[i][l] = x[i][l] + y[i][l]
# print(total)

