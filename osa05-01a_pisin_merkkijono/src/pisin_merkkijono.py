def pisin(l: list) -> str:
  longest = l[0]

  for w in l:
    if len(w) > len(longest):
      longest = w

  return longest