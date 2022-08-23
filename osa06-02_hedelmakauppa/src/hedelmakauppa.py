def lue_hedelmat():
  result = {}

  with open('hedelmat.csv') as csvfile:
    for line in csvfile:
      line = line.replace('\n', '')
      parts = line.split(';')
      result[parts[0]] = float(parts[1])

  return result