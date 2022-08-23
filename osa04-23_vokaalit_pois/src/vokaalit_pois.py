def ilman_vokaaleja(s:str) -> str:
  vocals = ['a', 'ä', 'å', 'o', 'ö', 'u', 'y', 'e', 'i']

  for v in vocals:
    s = s.replace(v, '')

  return s