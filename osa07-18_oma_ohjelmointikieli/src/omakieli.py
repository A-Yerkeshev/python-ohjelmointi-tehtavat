def suorita(program:list) -> list:
  # Prepare variables
  variables = {'A': 0,'B': 0,'C': 0,'D': 0,'E': 0,'F': 0,'G': 0,'H': 0,'I': 0,'J': 0,'K': 0,
    'L': 0,'M': 0,'N': 0,'O': 0,'P': 0,'R': 0,'Q': 0,'S': 0,'T': 0,'U': 0,'V': 0,'W': 0,'X': 0,
    'Y': 0,'Z': 0,
  }
  points = {}
  prints = []
  pointer = 0

  # Define program points
  for command in program:
    parts = command.split(' ')
    if len(parts) == 1 and parts[0] != 'END':
      points[parts[0][:-1]] = program.index(command)

  # Execute commands
  while pointer < len(program):
    command = program[pointer]
    parts = command.split(' ')
    verb = parts[0]

    if verb == 'PRINT':
      val = variables[parts[1]] if parts[1] in variables else int(parts[1])
      prints.append(val)

    elif verb == 'MOV':
      val = parts[2]
      variables[parts[1]] = variables[val] if val in variables else int(val)

    elif verb == 'ADD':
      val = parts[2]
      variables[parts[1]] += variables[val] if val in variables else int(val)

    elif verb == 'SUB':
      val = parts[2]
      variables[parts[1]] -= variables[val] if val in variables else int(val)

    elif verb == 'MUL':
      val = parts[2]
      variables[parts[1]] *= variables[val] if val in variables else int(val)

    elif verb == 'JUMP':
      pointer = points[parts[1]]

    elif verb == 'IF':
      condition = parts[1:4]
      oper = condition[1]
      val1 = variables[condition[0]] if condition[0] in variables else int(condition[0])
      val2 = variables[condition[2]] if condition[2] in variables else int(condition[2])
      evl = False

      if oper == '==':
        if val1 == val2:
          evl = True
      elif oper == '!=':
        if val1 != val2:
          evl = True
      elif oper == '<':
        if val1 < val2:
          evl = True
      elif oper == '>':
        if val1 > val2:
          evl = True
      elif oper == '<=':
        if val1 <= val2:
          evl = True
      elif oper == '>=':
        if val1 >= val2:
          evl = True

      if evl:
        pointer = points[parts[5]]

    elif verb == 'END':
      return prints

    pointer += 1

  return prints

