def poista_isot(l:list) -> list:
  result = []

  for w in l:
    if not w.isupper():
      result.append(w)

  return result

