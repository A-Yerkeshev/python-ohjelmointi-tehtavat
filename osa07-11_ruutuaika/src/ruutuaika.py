from datetime import datetime, timedelta

filename = input('Tiedosto:')
begins = datetime.strptime(input('Aloituspäivä:'), "%d.%m.%Y")
days = int(input('Montako päivää:'))
print('Anna ruutuajat kunakin päivänä minuutteina (TV tietokone mobiililaite):')

periods = {}
for i in range(0, days):
  date = (begins + timedelta(days=i)).strftime("%d.%m.%Y")
  time = input(f'Ruutuaika {date}:').split(' ')
  periods[date] = time

total_minutes = 0
for date, time in periods.items():
  for t in time:
    total_minutes += int(t)

with open(filename, 'w') as file:
  file.write(f'Ajanjakso: {begins.strftime("%d.%m.%Y")}-{(begins + timedelta(days=days-1)).strftime("%d.%m.%Y")}\n')
  file.write(f'Yht. minuutteja: {total_minutes}\n')
  file.write(f'Keskim. minuutteja: {total_minutes/len(periods)}\n')
  for date, time in periods.items():
    file.write(f"{date}: {'/'.join(time)}\n")

print('Tiedot tallennettu tiedostoon', filename)