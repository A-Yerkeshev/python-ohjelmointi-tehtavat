def sarake_oikein(matrix: list, col_num: int) -> bool:
  col = []
  res = True

  for row in matrix:
    col.append(row[col_num])

  for num in range(1,10):
    if col.count(num) > 1:
      res = False
      break

  print(col)

  return res
