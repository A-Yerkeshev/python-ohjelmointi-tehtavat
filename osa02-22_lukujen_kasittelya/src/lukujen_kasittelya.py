print('Syötä kokonaislukuja, 0 lopettaa:')

n = int(input('Luku:'))

pos = 0
neg = 0
summ = 0

while n != 0:
    if n > 0:
        pos += 1
    else:
        neg += 1

    summ += n

    n = int(input('Luku:'))

print('... lukujen kysely')
print('Lukuja yhteensä', pos+neg)
print('Lukujen summa', summ)
print('Lukujen keskiarvo', summ/(pos+neg))
print('Positiivisia', pos)
print('Negatiivisia', neg)
