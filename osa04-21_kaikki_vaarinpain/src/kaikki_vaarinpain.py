def kaikki_vaarinpain(l:list) -> list:
  result = []
  l = l[::-1]

  for w in l:
    result.append(w[::-1])

  return result
