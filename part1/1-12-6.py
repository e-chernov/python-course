num = input()
last = num[len(num) - 1]
string = ' программист'

if last == '2' or last == '3' or last == '4':
    if num[len(num) - 2] != '1':
        string += 'а'
    else:
        string += 'ов'
elif last == '5' or last == '6' or last == '7' or last == '8' or last == '9' or last == '0':
    string += 'ов'
else:
    if len(num) != 1 and num[len(num) - 2] == '1':
        string += 'ов'

print(num + string)