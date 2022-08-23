def lue(prompt:str, lowest:int, highest:int):
  try:
    num = int(input(prompt))
  except ValueError:
    num = ''

  while type(num) != int or num>highest or num<lowest:
    print(f'Syötteen on oltava kokonaisluku väliltä {lowest}...{highest}')
    try:
      num = int(input(prompt))
    except ValueError:
      pass

  return num
