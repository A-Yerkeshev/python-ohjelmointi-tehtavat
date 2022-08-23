def pelaa_siirto(desk:list, col_i:int, row_i:int, val:str):
  if (row_i > 2 or row_i < 0
  or col_i > 2 or col_i < 0
  or not desk[row_i][col_i] == ''):
    return False
  else:
    desk[row_i][col_i] = val
    return True
