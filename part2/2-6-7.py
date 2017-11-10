sum = int(input())
sqr = [sum * sum]

while sum != 0:
    num = int(input())
    sum += num
    sqr.append(num * num)

sum = 0
for i in range(0, len(sqr)):
    sum += sqr[i]
print(sum)