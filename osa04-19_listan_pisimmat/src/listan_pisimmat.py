def pisimmat(words: list) -> list:
  # This approach uses twice more memory but twice less time
  result = words.copy()
  maxlen = 0

  for word in words:
    if len(word) > maxlen:
      maxlen = len(word)
    # If word's length is smaller than maxlen it never can be included into answer
    elif len(word) < maxlen:
      result.remove(word)

  # By now result list has values in ascending order
  # Now slice last equal-sized values of result list

  i = -1
  while i>-len(result) and len(result[i]) == len(result[i-1]):
    i -= 1
  result = result[i:]

  return result
