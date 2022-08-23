y = int(input('Vuosi:'))
n = y+1
leap = False

while not leap:
    if n%100 == 0:
        if n%400 == 0:
            leap = True
        else:
            leap = False
    elif n%4 == 0:
        leap = True
    else:
        leap = False

    if leap:
        print(f'Vuotta {y} seuraava karkausvuosi on {n}')
        break

    n += 1


