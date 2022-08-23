n = int(input('Anna luku: '))

while n>0:
    fac = 1
    i = n
    while i>0:
        fac *= i
        i -= 1
    
    print(f'Luvun {n} kertoma on {fac}')
    n = int(input('Anna luku: '))

print('Kiitos ja moi!')
