import string
from random import choice

def luo_salasana(ln:int) -> str:
  res = ''
  for i in range(0, ln):
    res += choice(string.ascii_lowercase)
  return res