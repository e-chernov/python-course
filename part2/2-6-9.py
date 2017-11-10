arr = [int(i) for i in input().split()]
num = int(input())

output = []

for i in range(0, len(arr)):
    if arr[i] == num:
        output.append(str(i))

if len(output) == 0:
    output.append('Отсутствует')

print(' '.join(output))