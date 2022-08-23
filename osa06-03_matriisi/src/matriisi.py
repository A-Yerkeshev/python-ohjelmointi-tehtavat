def read_matrix():
  matrix = []

  with open('matriisi.txt') as txtfile:
    for line in txtfile:
      line = line.replace('\n', '')
      strlist = line.split(',')
      numlist = []
      for s in strlist:
        numlist.append(int(s))
      matrix.append(numlist)

  return matrix

def summa():
  linesums = rivisummat()
  return sum(linesums)

def maksimi():
  matrix = read_matrix()
  largest = 0

  for line in matrix:
    for num in line:
      if num > largest:
        largest = num

  return largest

def rivisummat():
  matrix = read_matrix()
  result = []

  for line in matrix:
    result.append(sum(line))

  return result