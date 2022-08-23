y = int(input('Anna vuosi: '))

if y%4 == 0:
    if y%100==0:
        if y%400==0:
            print('Vuosi on karkausvuosi.')
        else:
            print('Vuosi ei ole karkausvuosi.')
    else:
        print('Vuosi on karkausvuosi.')
else:
    print('Vuosi ei ole karkausvuosi.')
