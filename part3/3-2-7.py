n = int(input())
results = {}
for i in range(1, n + 1):
    if i in results:
        print(result[i])
    else:
        result = f(int(input()))
        results[i] = result
        print(result)