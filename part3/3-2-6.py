lst = input().lower().split()
d = {}

for i in lst:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for key in d:
    print(key, d[key])

