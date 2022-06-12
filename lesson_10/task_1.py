from random import randint


class Matrix:


    def __init__(self, width, height):
        self._matrix = []
        self.__width = width
        self.__height = height
        for i in range(height):
            self._matrix.append(list())
            for _ in range(width):
                self._matrix[i].append(randint(-100, 100))

    def __str__(self):
        res = ''
        for i in range(self.__height):
            res += '|'
            for j in range(self.__width):
                res += f'{self._matrix[i][j]:^5}'
            res += '|\n'
        return res

    def __add__(self, other):
        if (self.__height != other.__height) or \
            (self.__width != other.__width):
            raise ValueError('Матрицы разной размерности')
        
        res = Matrix(self.__width, self.__height)

        for i in range(self.__height):
            for j in range(self.__width):
                res._matrix[i][j] = self._matrix[i][j] + \
                                     other._matrix[i][j]

        return res



if __name__ == '__main__':
    m1 = Matrix(5, 4)
    m2 = Matrix(5, 4)
    print(m1, m2, sep='\n')
    print(type(m1+m2), m1+m2, sep='\n')