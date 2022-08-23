def eniten_kirjainta(s:str) -> int:
  res = ''
  count = 0

  for c in s:
    if c != res:
      if s.count(c) > count:
        res = c
        count = s.count(c)

  return res
