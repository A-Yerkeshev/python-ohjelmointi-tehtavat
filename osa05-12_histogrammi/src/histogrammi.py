def histogrammi(s:str):
  occur = {}

  for c in s:
    if c not in occur:
      occur[c] = 0
    occur[c] += 1

  for key in occur:
    print(key, '*'*occur[key])