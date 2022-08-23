def rivi_oikein(matrix: list, line_num: int) -> bool:
  res = True

  for num in range(1,10):
    if matrix[line_num].count(num) > 1:
      res = False
      break

  return res

