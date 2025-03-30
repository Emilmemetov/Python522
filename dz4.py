import math

circle_area = (lambda a: math.pi * a ** 2)
rectangle_area = (lambda b, c: b * c)
trapezoid_area = (lambda a, b, h: 0.5 * (a + b) * h)

print("Площадь окружности радиуса 2:", circle_area(2))
print("Площадь прямоугольника размером 10*13:", rectangle_area(10, 13))
print("Площадь трапеции для a=7, b=5, h=3:", trapezoid_area(7, 5, 3))


# print(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
