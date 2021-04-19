"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод __init__()), который должен принимать данные (список списков)
для формирования матрицы. Следующий шаг — реализовать перегрузку метода __str__()
для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса
Matrix (двух матриц). Результатом сложения должна быть новая матрица.
"""


class Matrix:
    def __init__(self, matrix_list: list):
        self.matrix_list = matrix_list  # матрица - список списков

    def __str__(self):
        return 'Матрица:\n' + '\n'.join('\t'.join(map(str, el_row))
                    for el_row in self.matrix_list)

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise ArithmeticError("Второй опранд не матрица")
        try:
            el_row_left = [el_row_left for el_row_left in self.matrix_list]
            el_row_right = [el_row_right for el_row_right in other.matrix_list]
            sum_list = []
            for el_left_row, el_right_row in zip(el_row_left, el_row_right):
                sum_list_row = []
                for el_left, el_right in zip(el_left_row, el_right_row):                    sum_list_row.append(el_left + el_right)
                sum_list.append(sum_list_row)
        except IndexError:
            return "Матрицы должны быть одной размерности"
        except StopIteration:
            return "Матрицы должны быть одной размерности"
        return Matrix(sum_list)


def create_matrix(numb_el, n=1, m=1):
    """ создает матрицу размерности nхm
    :param numb_el: число, цифры которого войдут в матрицу
    :param n: число строк
    :param m: число столбцов
    :return: список списков по строкам матрицы
    """
    digits, num_matrix, res_matrix, row_matrix = 0, [], [], []
    while numb_el:
        num_matrix.append(numb_el % 10)
        numb_el = numb_el // 10
        digits += 1
    if digits == m * n:
        for el in num_matrix[::-1]:
            if len(row_matrix) == m:
                res_matrix.append(row_matrix)
                row_matrix = []
            row_matrix.append(int(el))
        res_matrix.append(row_matrix)
    else:
        print("Размерность не соблюдена, так как",
              "столбцов", m, "строк", n, "чисел", digits)
    return res_matrix


right_mx = create_matrix(654321, 2, 3)
left_mx = create_matrix(123456, 2, 3)
print(Matrix(left_mx) + Matrix(right_mx))
