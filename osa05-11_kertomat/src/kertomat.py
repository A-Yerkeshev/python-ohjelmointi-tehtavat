import math

def kertomat(n:int) -> dict:
  result = {}

  for i in range(1, n+1):
    result[i] = math.factorial(i)

  return result
