def pisin_naapurijono(l:list) -> int:
  row = []
  res = 0

  for n in l:
    if row == [] or n-row[-1] == 1 or row[-1]-n == 1:
      row.append(n)
    else:
      row = [n]

    if len(row) > res:
      res = len(row)

  return res

if __name__ == "__main__":
  print(pisin_naapurijono([1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]))