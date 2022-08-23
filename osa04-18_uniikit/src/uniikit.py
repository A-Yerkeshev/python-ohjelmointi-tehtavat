def uniikit(l: list) -> list:
  result = []
  l.sort()

  for i in l:
    if i not in result:
      result.append(i)

  return result