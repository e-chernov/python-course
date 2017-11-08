entity = input()

if entity == 'треугольник':

    a = int(input())
    b = int(input())
    c = int(input())

    p = (a + b + c) / 2

    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)


elif entity == 'прямоугольник':

    a = int(input())
    b = int(input())

    print(a * b)


elif entity == 'круг':

    r = int(input())
    pi = 3.14

    print(pi * r ** 2)
    