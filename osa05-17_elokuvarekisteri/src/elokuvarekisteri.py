def lisaa_elokuva(register:list, name:str, director:str, year:int, length:int):
  movie = {
    'nimi': name,
    'ohjaaja': director,
    'vuosi': year,
    'pituus': length
  }
  register.append(movie)
