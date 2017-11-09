a = int(input())
b = int(input())
c = int(input())

if a > b:
    if a > c:
        max = a
        if b < c:
            min = b
            middle = c
        else:
            min = c
            middle = b
    else:
        max = c
        min = b
        middle = a
else:
    if b > c:
        max = b
        if a < c:
            min = a
            middle = c
        else:
            min = c
            middle = a
    else:
        max = c
        min = a
        middle = b

print(max)
print(min)
print(middle)
