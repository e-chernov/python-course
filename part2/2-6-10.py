string = ''
matrix = []
output = []


while string != 'end':
    string = input()
    if string != 'end':
        row = [int(i) for i in string.split()]
        matrix.append(row)


for i in matrix:
    for j in matrix[i]:
        outputRow = [int(j)]