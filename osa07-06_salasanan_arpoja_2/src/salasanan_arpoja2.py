import string
from random import choice, randint, shuffle

def luo_hyva_salasana(ln:int, nums:bool, sc:bool) -> str:
  res = []
  chars = string.ascii_lowercase
  # Generate 1 letter, and optionally 1 num and 1 special char
  res.append(choice(chars))
  if nums:
    res.append(choice(string.digits))
    chars += string.digits
  if sc:
    res.append(choice('!?=+-()#'))
    chars += '!?=+-()#'

  for i in range(len(res), ln):
    res.append(choice(chars))

  shuffle(res)
  return ''.join(res)