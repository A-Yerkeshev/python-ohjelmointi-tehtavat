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