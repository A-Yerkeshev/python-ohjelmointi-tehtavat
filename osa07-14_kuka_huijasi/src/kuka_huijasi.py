import csv
from datetime import datetime

def huijarit() -> list:
  test_starts = {}
  cheaters = []

  with open('tentin_aloitus.csv') as file:
    for line in csv.reader(file, delimiter=";"):
      test_starts[line[0]] = datetime.strptime(line[1], "%H:%M")

  with open('palautus.csv') as file:
    for line in csv.reader(file, delimiter=";"):
      if (datetime.strptime(line[3], "%H:%M") - test_starts[line[0]]).seconds/3600 > 3:
        if line[0] not in cheaters:
          cheaters.append(line[0])

  return cheaters