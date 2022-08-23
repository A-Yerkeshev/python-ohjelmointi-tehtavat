hrate = float(input('Tuntipalkka:'))
hours = int(input('Työtunnit:'))
wday = input('Viikonpäivä:')

total = hrate*hours

if wday == 'sunnuntai':
    total = total*2

print(f'Palkka {total} euroa')
