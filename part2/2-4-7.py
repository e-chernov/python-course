genome = input()
result = ''

i = 0
while i < len(genome):
    counter = 1
    j = i + 1
    while j < len(genome) and genome[j] == genome[i]:
        counter += 1
        j += 1
    if counter > 1:
        result += genome[i] + str(counter)
        i = j
    else:
        result += genome[i] + '1'
        i += 1

print(result)