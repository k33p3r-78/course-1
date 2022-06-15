from random import randint


class Matrix:


    def __init__(self, *args, width=None, height=None):
        self._matrix = []
        if width: self.__width = width
        if height: self.__height = height

        if not args and width and height:
            for i in range(height):
                self._matrix.append(list())
                for _ in range(width):
                    self._matrix[i].append(randint(-100, 100))
        elif args:
            for arr in args:
                self._matrix.append(arr)
            self.__height = len(args[0])
            self.__width = len(args[0][0])
        else:
            raise ValueError('Не указаны исходные данные и параметры размерности')

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
        
        res = Matrix(width=self.__width, height=self.__height)

        for i in range(self.__height):
            for j in range(self.__width):
                res._matrix[i][j] = self._matrix[i][j] + \
                                     other._matrix[i][j]

        return res



if __name__ == '__main__':
    m1 = Matrix(width=5, height=4)
    m2 = Matrix(width=5, height=4)
    print(m1, m2, sep='\n')
    print(type(m1+m2), m1+m2, sep='\n')




