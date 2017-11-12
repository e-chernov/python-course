with open('dataset_3363_3.txt') as inf:
    lst = []
    for line in inf:
        lst += line.strip().lower().split()

d = {}
for elem in lst:
    if elem not in d:
        d[elem] = 1
    else:
        d[elem] += 1

max = 0
maxElem = ''
for key in d:
    if d[key] > max or d[key] == max and key > maxElem:
        maxElem = key
        max = d[key]

with open('ouput_3_4_3.txt', 'w') as ouf:
    ouf.write(maxElem + ' ')
    ouf.write(str(max))




