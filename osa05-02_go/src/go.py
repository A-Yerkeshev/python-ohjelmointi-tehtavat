def kumpi_voitti(desk: list) -> int:
  black = 0
  white = 0

  for row in desk:
    black += row.count(1)
    white += row.count(2)

  if black > white:
    return 1
  elif white > black:
    return 2
  else:
    return 0
