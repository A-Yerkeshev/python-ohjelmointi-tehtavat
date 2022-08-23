def suodata_laskut():
  correct = []
  incorrect = []

  with open('laskut.csv') as file:
    for line in file:
      parts = line.strip().split(';')

      if '+' in parts[1]:
        operands = parts[1].split('+')
        operator = '+'
      elif '-' in parts[1]:
        operands = parts[1].split('-')
        operator = '-'

      if check_validity(int(operands[0]), operator, int(operands[1]), int(parts[2])):
        correct.append(line)
      else:
        incorrect.append(line)

  with open('oikeat.csv', 'w') as file:
    for entry in correct:
      file.write(entry)

  with open('vaarat.csv', 'w') as file:
    for entry in incorrect:
      file.write(entry)

def check_validity(num1:int, oper:str, num2:int, res:int) -> bool:
  if oper == '+':
    if num1 + num2 == res:
      return True
    else:
      return False
  elif oper == '-':
    if num1 - num2 == res:
      return True
    else:
      return False
  else:
    return False
