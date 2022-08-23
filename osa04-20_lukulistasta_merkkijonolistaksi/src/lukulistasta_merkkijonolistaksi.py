def muotoile(l:list) -> list:
  result = []
  for n in l:
    result.append(f'{n:.2f}')
  return result
