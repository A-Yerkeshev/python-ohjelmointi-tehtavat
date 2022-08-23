def lyhin(l: list) -> str:
  shortest = l[0]
  for w in l:
    if len(w) < len(shortest):
      shortest = w
  return shortest
