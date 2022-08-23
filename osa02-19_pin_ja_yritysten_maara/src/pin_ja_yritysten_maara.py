pin = input('PIN-koodi:')
tries = 1

while pin != '4321':
    print('Väärin')
    pin = input('PIN-koodi:')
    tries += 1

if tries > 1:
    print(f'Oikein, tarvitsit {tries} yritystä')
else:
    print('Oikein, tarvitsit vain yhden yrityksen!')
