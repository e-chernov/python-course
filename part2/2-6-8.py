n = int(input())
output = []

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if len(output) >= n:
            break
        output.append(str(i))

print(' '.join(output))