s1 = input('Anna jono 1:')
s2 = input('Anna jono 2:')

if len(s1) == len(s2):
    print('Jonot ovat yhtä pitkät')
elif len(s1) > len(s2):
    print(f'{s1} on pidempi')
else:
    print(f'{s2} on pidempi')
