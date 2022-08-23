def suurin():
  with open('luvut.txt') as textfile:
    largest = 0

    for num in textfile:
      if int(num) > largest:
        largest = int(num)

  return largest