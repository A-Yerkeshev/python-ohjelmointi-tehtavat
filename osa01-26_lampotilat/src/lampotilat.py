f = int(input('Anna lämpötila (F):'))
c = (f-32)*5/9

print(f'{f} fahrenheit-astetta on {c} celsius-astetta')

if (c < 0):
    print('Paleltaa!')
