def kertaa_kymmenen(start: int, end: int) -> dict:
  result = {}

  for i in range(start, end+1):
    result[i] = i*10

  return result
