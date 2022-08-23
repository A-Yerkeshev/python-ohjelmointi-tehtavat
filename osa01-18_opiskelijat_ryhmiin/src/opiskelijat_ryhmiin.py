# Kirjoita ratkaisu tähän
studnum = int(input('Montako opiskelijaa?'))
groupsize = int(input('Mikä on ryhmän koko?'))
print('Ryhmien määrä:', (studnum + groupsize - 1)//groupsize)