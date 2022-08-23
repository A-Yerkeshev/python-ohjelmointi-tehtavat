print('Henkilö 1:')
n1 = input('Nimi:')
a1 = int(input('Ikä:'))
print('Henkilö 2:')
n2 = input('Nimi:')
a2 = int(input('Ikä:'))
if a1>a2:
    print('Vanhempi on', n1)
elif a2>a1:
    print('Vanhempi on', n2)
else:
    print(f'{n1} ja {n2} ovat yhtä vanhoja')
