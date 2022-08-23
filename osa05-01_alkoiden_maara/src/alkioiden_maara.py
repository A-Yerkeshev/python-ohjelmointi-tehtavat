def laske_alkiot(matrix: list, search: int) -> int:
  count = 0

  for row in matrix:
    count += row.count(search)

  return count
