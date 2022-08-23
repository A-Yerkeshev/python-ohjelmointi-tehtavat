l1 = input('Anna 1. kirjain:')
l2 = input('Anna 2. kirjain:')
l3 = input('Anna 3. kirjain:')

if l1 > l2:
    if l1 > l3:
        # l1 is last
        if l2 > l3:
            mid = l2
        else:
            mid = l3
    else:
        mid = l1
elif l1 > l3:
    #l3 < l1 <l2
    mid = l1
else:
    #l1 is first
    if l2 > l3:
        mid = l3
    else:
        mid = l2

print('Keskimmäinen kirjain on', mid)

