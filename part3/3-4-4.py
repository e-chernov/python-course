with open('dataset_3363_4.txt') as inf:
    lst = []
    for line in inf:
        lst.append(line.strip().split(';'))

for item in lst:
    item.append((int(item[1]) + int(item[2]) + int(item[3])) / 3)

math_sum = 0
phis_sum = 0
rus_sum = 0
for i in range(0, len(lst)):
    math_sum += int(lst[i][1])
    phis_sum += int(lst[i][2])
    rus_sum += int(lst[i][3])
math_av = math_sum / len(lst)
phis_av = phis_sum / len(lst)
rus_av = rus_sum / len(lst)

with open('output_3_4_4.txt', 'w') as ouf:
    for item in lst:
        ouf.write(str(item[4]) + '\n')
    ouf.write(str(math_av) + ' ')
    ouf.write(str(phis_av) + ' ')
    ouf.write(str(rus_av))
