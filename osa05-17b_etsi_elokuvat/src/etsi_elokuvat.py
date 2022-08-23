def etsi_elokuvat(register:list, search:str) -> list:
  result = []

  for movie in register:
    if search.lower() in movie['nimi'].lower():
      result.append(movie)

  return result
