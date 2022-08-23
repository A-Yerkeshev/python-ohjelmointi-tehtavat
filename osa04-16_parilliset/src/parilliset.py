def parilliset(l: list) -> list:
  result = []

  for n in l:
    if int(n)%2 == 0:
      result.append(n)

  return result
