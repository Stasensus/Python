# 5.Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

x1 = int(input('Введите координаты первой точки по оси Х: '))
y1 = int(input('Введите координаты первой точки по оси Y: '))
x2 = int(input('Введите координаты второй точки по оси Х: '))
y2 = int(input('Введите координаты второй точки по оси Y: '))
z = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
# print(f"Длина отрезка: {format(z, '.2f')}")
z = z // 0.01 / 100
print (round(z, 2))
# В одном варианте выдачи выходит 5.10, в другом 5.1, но ни в одном не выходит 5.09 как в примере из задачи. Пришлось разделить без остатка на 0,01, чтобы округлить таким образом