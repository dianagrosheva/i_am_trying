print('Введите 3 числа')
def triangle_type ():
    a = int(input())
    b = int(input())
    c = int(input())
    if a + b > c and a + c > b and b + c > a:
        if a != b != c and a != c != b:
            print('Прямоугольный треугольник')
        elif a == b == c:
            print('Равносторонний треугольник')
        else:
            print('Равнобедренный треугольник')
    else:
        print('Ты долбаеб, такого не существует')

triangle_type()
