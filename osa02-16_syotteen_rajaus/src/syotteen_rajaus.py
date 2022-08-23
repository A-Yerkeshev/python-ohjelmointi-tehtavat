from math import sqrt

n = int(input('Syötä luku:'))

while n != 0:
    if n<0:
        print('Epäkelpo luku')
    else:
        print(sqrt(n))
    n = int(input('Syötä luku:'))

print('Lopetetaan...')