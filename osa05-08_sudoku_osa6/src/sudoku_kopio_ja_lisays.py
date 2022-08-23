def tulosta(grid: list):
  for row_i in range(len(grid)):
    for cell_i in range(len(grid[row_i])):
      if grid[row_i][cell_i] > 0:
        print(grid[row_i][cell_i], end=' ')
      else:
        print('_', end=' ')
      if (cell_i-2)%3 == 0:
        print(' ', end='')
    print()
    if (row_i-2)%3 == 0:
      print()

def kopioi_ja_lisaa(grid:list, row_i:int, col_i:int, val:int):
  new_grid = []

  # grid.copy() creates just a shallow copy of list, which means
  # that each new_grid[row] is reference to grid[row], not a copy of it!
  for row in grid:
    new_grid.append(row.copy())

  new_grid[row_i][col_i] = val

  return new_grid
