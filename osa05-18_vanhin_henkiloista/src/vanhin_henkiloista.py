def vanhin(personnel:list) -> str:
  oldest = personnel[0]

  for pers in personnel:
    if pers[1] < oldest[1]:
      oldest = pers

  return oldest[0]