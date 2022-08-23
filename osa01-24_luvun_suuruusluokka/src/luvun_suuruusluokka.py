# Kirjoita ratkaisu tähän
num = int(input('Anna luku:'))

magn = 1000

while magn >= 10:
    if num < magn:
        print('Luku on pienempi kuin', magn)
        magn = magn//10
    else:
        magn = 0

print('Kiitos!')