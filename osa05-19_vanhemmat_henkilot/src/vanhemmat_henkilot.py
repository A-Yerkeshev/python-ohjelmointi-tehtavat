def vanhemmat(personnel:list, year:int) -> list:
  oldest = []

  for pers in personnel:
    if pers[1] < year:
      oldest.append(pers[0])

  return oldest
