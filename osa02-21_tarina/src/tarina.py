w = input('Anna sana:')
last = ''
output = ''

while w != last and w != 'loppu':
    output = output + w + ' '
    last = w
    w = input('Anna sana:')

print(output)