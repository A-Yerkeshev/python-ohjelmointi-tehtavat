def transponoi(matrix: list):
  # Prepare empty matrix
  new_matrix = []

  for c in matrix[0]:
    new_matrix.append([])

  # Fill new_matrix rows with values from matrix columns
  for row_i in range(len(matrix)):
    for col_i in range(len(matrix[row_i])):
      new_matrix[col_i].append(matrix[row_i][col_i])

  matrix[:] = new_matrix