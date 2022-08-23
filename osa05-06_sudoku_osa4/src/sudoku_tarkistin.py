def sudoku_oikein(matrix: list) -> bool:
  # Check rows and columns
  for i in range(0, len(matrix)):
    if not rivi_oikein(matrix, i) or not sarake_oikein(matrix, i):
      return False

  # Check squares
  for x in range(0, 7, 3):
    for y in range(0, 7, 3):
      if not nelio_oikein(matrix, x, y):
        return False

  return True

def rivi_oikein(matrix: list, line_num: int) -> bool:
  res = True

  for num in range(1,10):
    if matrix[line_num].count(num) > 1:
      res = False
      break

  return res
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
def nelio_oikein(matrix: list, line_num: int, col_num: int) -> bool:
  # Extract 3x3 sub-matrix
  sub_matrix = []

  for r in range(0,3):
    sub_row = []
    for c in range(0,3):
      sub_row.append(matrix[line_num+r][col_num+c])
    sub_matrix.append(sub_row)

  for num in range(1,10):
    count = 0

    for row in sub_matrix:
      count += row.count(num)
      if count > 1:
        return False

  return True