with open('dataset_3363_2.txt') as inf:
    s = list(inf.readline())

result = []
issecond = False

for i in range(0, len(s)):
    if s[i].isdigit():
        if issecond:
            issecond = False
            continue
        temp = [s[i]]
        j = 1
        next_elem = s[i + j]
        while next_elem.isdigit():
            temp += [next_elem]
            j += 1
            next_elem = s[i + j]
        if len(temp) == 2:
            issecond = True

        for k in range(int(''.join(temp))):
            result.append(s[i - 1])

with open('output.txt', 'w') as ouf:
    ouf.write(''.join(result))