# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math
 
class Triangle(object):
    def __init__(self, a, b, c):
        # Данная функция вычисляет длину стороны согласно координатам точек
        def sideLen(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2
                             + (dot1[1] - dot2[1]) ** 2)
 
        self.a = a
        self.b = b
        self.c = c
        # В соответствии с соседними координатами вычисляем длину стороны ab
        self.ab = sideLen(self.a, self.b)
        self.bc = sideLen(self.b, self.c)
        self.ca = sideLen(self.c, self.a)
 
    # Применим формулу Герона для вычесления площади треугольника 
    def areaTriangle(self):
        semi_perimeter = self.perimeterTriangle() / 2
 
        return math.sqrt(semi_perimeter
                         * (semi_perimeter - self.ab)
                         * (semi_perimeter - self.bc)
                         * (semi_perimeter - self.ca))


    # Вычисляем высоту треугольника
    def heightTriangle(self):
        return self.areaTriangle() / (self.ab / 2)


    # Вычисляем периметр треугольника
    def perimeterTriangle(self):
        return self.ab + self.bc + self.ca
 
    
treygolnik1 = Triangle((5, 4), (8, 10), (1, 14))
 
print(treygolnik1.areaTriangle())
print(treygolnik1.heightTriangle())
print(treygolnik1.perimeterTriangle())

# Результат
26.999999999999986
8.049844718999239
25.540791295066924


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
