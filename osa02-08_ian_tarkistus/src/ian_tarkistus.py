a = int(input('Kerro ikäsi? '))

if a<0:
    print('Taitaa olla virhe')
elif a<5:
    print('En usko, että osaat kirjoittaa...')
else:
    print(f'Ok, olet siis {a}-vuotias')
