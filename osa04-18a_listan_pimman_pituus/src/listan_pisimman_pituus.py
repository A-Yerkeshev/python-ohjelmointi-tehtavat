def pisimman_pituus(l: list) -> int:
  longest = len(l[0])
  for w in l:
    if len(w) > longest:
      longest = len(w)
  return longest