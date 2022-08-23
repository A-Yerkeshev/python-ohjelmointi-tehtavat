print('Kerro huominen sääennuste:')

tpr = int(input('Lämpötila:'))
rains = input('Sataako (kyllä/ei):')

print('Pue housut ja t-paita')

if tpr <= 20:
    print('Ota myös pitkähihainen paita')
if tpr <= 10:
    print('Pue päälle takki')
if tpr <= 5:
    print('Suosittelen lämmintä takkia')
    print('Kannattaa ottaa myös hanskat')
if rains == 'kyllä':
    print('Muista sateenvarjo!')


