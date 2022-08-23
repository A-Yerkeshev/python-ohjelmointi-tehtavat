def hae_sanat(search: str) -> list:
  dictionary = build_dict()
  result = []

  if search.startswith('*'):
    for word in dictionary:
      if word.endswith(search[1:]):
        result.append(word)
  elif search.endswith('*'):
    for word in dictionary:
      if word.startswith(search[:-1]):
        result.append(word)
  elif '.' in search:
    for word in dictionary:
      match = True

      if len(word) != len(search):
        match = False
        continue

      for i in range(len(search)):
        if search[i] != '.' and search[i] != word[i]:
          match = False
          break

      if match:
        result.append(word)
  else:
    if search in dictionary:
      result.append(search)

  return result

def build_dict() -> list:
  result = []
  with open('sanat.txt') as file:
    for line in file:
      result.append(line.strip())
  return result