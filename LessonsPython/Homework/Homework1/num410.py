# 1.ввести радиус круга и сторону квадрата
# 2.расчитать площади круга и квадрата
# 3.сравнить площади
# 4.написать, что больше

circle_radius = 0
square_side = 0

circle_radius = int( input("ввести радиус круга: "))
square_side = int( input("ввести сторону квадрата: "))

area_circle = circle_radius * circle_radius * 3.14
area_square = square_side * square_side

if area_circle > area_square:
    print(f"площадь круга больше")
else:
    print(f"площадь квадрата больше")