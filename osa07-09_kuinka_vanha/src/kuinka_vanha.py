from datetime import datetime

day = int(input('Päivä:'))
month = int(input('Kuukausi:'))
year = int(input('Vuosi:'))

birth_date = datetime(year, month, day)
millenium = datetime(1999, 12, 31)
diff = millenium-birth_date

if diff.days > 0:
  print(f'Olit {diff.days} päivää vanha, kun vuosituhat vaihtui.')
else:
  print('Et ollut syntynyt, kun vuosituhat vaihtui.')