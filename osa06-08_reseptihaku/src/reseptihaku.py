def read_recepies(filename:str) -> dict:
  recepies = {}

  with open(filename) as textfile:
    for line in textfile:
      line = line.strip()

      if line == '':
        name = ''
      elif line[0].isupper():
        name = line
        recepies[name] = {}
      elif line.isdigit():
        recepies[name]['prep_time'] = int(line)
      else:
        if 'ingridients' not in recepies[name]:
          recepies[name]['ingridients'] = [line]
        else:
          recepies[name]['ingridients'].append(line)

  return recepies

def hae_nimi(filename:str, search:str) -> list:
  recepies = read_recepies(filename)
  result = []

  for name in recepies:
    if search.lower() in name.lower() and search != '':
      result.append(name)

  return result

def hae_aika(filename:str, time:int) -> list:
  recepies = read_recepies(filename)
  result = []

  for name, data in recepies.items():
    if data['prep_time'] <= time:
      result.append(f"{name}, valmistusaika {data['prep_time']} min")

  return result

def hae_raakaaine(filename:str, ingr:str) -> list:
  recepies = read_recepies(filename)
  result = []

  for name, data in recepies.items():
    if ingr in data['ingridients']:
      result.append(f"{name}, valmistusaika {data['prep_time']} min")

  return result