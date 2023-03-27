import math

print('Введите 3 коэффициента квадратного уравнения:')
print("ax^2 + bx + c = 0:")

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

D = b**2 - 4*a*c

if D > 0:
    x1 = (-b - math.sqrt(D)) / (a * 2)
    x2 = (-b + math.sqrt(D)) / (a * 2)
    print ('D =', int(D),'x1 =', '%.2f' % x1, 'x2 =', '%.2f' % x2)

elif D == 0:
    x = -b / (2 * a)
    print ('Дискриминант =', int(D),'x =', '%.2f' % x)
else:
    print ('Корней нет')
