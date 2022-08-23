password = input('Salasana:')
passrep = input('Toista salasana:')

while passrep != password:
    print('Ei ollut sama!')
    passrep = input('Toista salasana:')

print('Käyttäjätunnus luotu!')
