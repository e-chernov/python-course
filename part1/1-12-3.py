num1 = float(input())
num2 = float(input())
op = input()

if op == '+' :
  print(num1 + num2)
elif op == '-' :
  print(num1 - num2)
elif op == '*' :
  print(num1 * num2)
elif op == '/' :
  if num2 == 0 :
    print('Деление на 0!')
  else :
    print(num1 / num2)
elif op == 'mod' :
  if num2 == 0 :
    print('Деление на 0!')
  else :
    print(num1 % num2)
elif op == 'pow' :
  print(num1 ** num2)
elif op == 'div' :
  if num2 == 0 :
    print('Деление на 0!')
  else :
    print(num1 // num2)