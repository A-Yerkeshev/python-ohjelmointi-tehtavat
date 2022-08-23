def summa(l1: list, l2: list) -> list:
  result = []

  for i in range(len(l1)):
    result.append(int(l1[i]) + int(l2[i]))

  return result
