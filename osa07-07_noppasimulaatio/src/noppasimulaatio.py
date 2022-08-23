from random import choice

def heita(die: str) -> int:
  dies = {
    'A': [3, 3, 3, 3, 3, 6],
    'B': [2, 2, 2, 5, 5, 5],
    'C': [1, 4, 4, 4, 4, 4]
  }
  return choice(dies[die])

def pelaa(die1: str, die2: str, times: int) -> tuple:
  win1 = 0
  win2 = 0
  draws = 0

  for i in range(0, times):
    res = (heita(die1), heita(die2))
    if res[0] > res[1]:
      win1 += 1
    elif res[1] > res[0]:
      win2 += 1
    else:
      draws += 1

  return (win1, win2, draws)
