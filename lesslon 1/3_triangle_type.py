print('Введите 3 числа')
a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    if c**2 == a**2 + b**2 or b**2 == a**2 + c**2 or a**2 == c**2 + b**2:
        print('Прямоугольный треугольник')
    elif a == b == c:
        print('Равносторонний треугольник')
    elif a == b or a == c or b == c:
        print('Равнобедренный треугольник')
    else:
        print('Просто треугольник')
else:
    print('Ты долбаеб, такого не существует')
