arr = input().split()
withoutRepeat = []
output = []
withoutRepeat.append(arr[0])

for i in range(1, len(arr)):
    if arr[i] in withoutRepeat:
        if arr[i] not in output:
            output.append(arr[i])
    withoutRepeat.append(arr[i])

print(' '.join(output))