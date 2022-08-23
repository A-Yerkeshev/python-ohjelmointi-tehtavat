import math

def hae_asematiedot(filename: str) -> dict:
  result = {}

  with open(filename) as file:
    for line in file:
      line = line.strip()
      parts = line.split(';')

      if parts[0] == 'Longitude':
        continue

      name = parts[3]
      lon = float(parts[0])
      lat = float(parts[1])

      result[name] = (lon, lat)

  return result

def etaisyys(stations: dict, stat1_name: str, stat2_name: str) -> float:
  stat1 = stations[stat1_name]
  stat2 = stations[stat2_name]

  x = (stat1[0] - stat2[0]) * 55.26
  y = (stat1[1] - stat2[1]) * 111.2

  return math.sqrt(x**2 + y**2)

def suurin_etaisyys(stations: dict) -> tuple:
  station_names = list(stations)
  distances = []

  for i in range(0, len(station_names)):
    name1 = station_names[i]
    for j in range(i+1, len(station_names)):
      name2 = station_names[j]
      distances.append((name1, name2, etaisyys(stations, name1, name2)))

  farest = (station_names[0], station_names[1], 0)
  for entry in distances:
    if entry[2] > farest[2]:
      farest = entry

  return farest