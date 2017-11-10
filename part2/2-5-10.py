arr = input().split()
output = []

if len(arr) > 1:
    for i in range(0, len(arr)):
        if i == len(arr) - 1:
            output.append(str(int(arr[0]) + int(arr[i - 1])))
        else:
            output.append(str(int(arr[i + 1]) + int(arr[i - 1])))
    outputStr = ' '.join(output)
    print(outputStr)
else:
    print(arr[0])