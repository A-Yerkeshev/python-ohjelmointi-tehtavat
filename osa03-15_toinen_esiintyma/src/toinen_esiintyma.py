st = input('Anna merkkijono:')
ss = input('Anna osajono:')

i = st.find(ss)
i = st.find(ss, i+len(ss))

if i != -1:
    print(f'Osajonon toinen esiintymä on kohdassa {i}.')
else:
    print('Osajono ei esiinny merkkijonossa kahdesti.')
