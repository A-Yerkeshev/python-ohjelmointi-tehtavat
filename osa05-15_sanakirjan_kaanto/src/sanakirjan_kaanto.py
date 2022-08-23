def kaanna(dictionary: dict):
  tmp = {}

  for key in dictionary:
    tmp[dictionary[key]] = key

  dictionary.clear()

  for key in tmp:
    dictionary[key] = tmp[key]
