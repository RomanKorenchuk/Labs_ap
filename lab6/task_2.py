def sort_decorator(func):
    def wrapper(self, *args, **kwargs):
        self.sort_columns()
        return func(self, *args, **kwargs)
    return wrapper


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    def calculate_fi(self):
        n = len(self.matrix)
        fi_values = []
        for i in range(n):
            product = 1
            for j in range(n - i - 1, n):
                product = product * self.matrix[i][j]
            fi_values.append(product)
        return fi_values

    @sort_decorator
    def sort_columns(self):
        rows, cols = len(self.matrix), len(self.matrix[0])
        for col in range(cols):
            for i in range(rows - 1):
                for j in range(rows - i - 1):
                    if self.matrix[j][col] < self.matrix[j + 1][col]:
                        self.matrix[j][col], self.matrix[j + 1][col] = self.matrix[j + 1][col], self.matrix[j][col]

    def calculate_F(self, fi_values):
        total = 0
        count = 0
        for value in fi_values:
            total += value
            count += 1
        return total / count

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Матриці мають різний розмір.")
        
        result = []
        for i in range(len(self.matrix)):
            row = [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
            result.append(row)
        return Matrix(result)

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])


matrix_data = [
    [-1, -5, -47, -8, -1],
    [-4, -98, -90, -45, -78],
    [-3, -2, -5, -9, -4],
    [-8, -67, -33, -91, -40],
    [-2, -58, -11, -65, -77]
]

matrix_obj = Matrix(matrix_data)

fi_values = matrix_obj.calculate_fi()
print("fi(aij):", fi_values)

sorted_matrix = matrix_obj.matrix 
print("\nВідсортована матриця:")
print(matrix_obj)

F_value = matrix_obj.calculate_F(fi_values)
print("\nЗначення F(fi(aij)):", F_value)

# Створення іншої матриці для перевірки перевантаження оператора +
matrix_data2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

matrix_obj2 = Matrix(matrix_data2)
summed_matrix = matrix_obj + matrix_obj2
print("\nСума двох матриць:")
print(summed_matrix)