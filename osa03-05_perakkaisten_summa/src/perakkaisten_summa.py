n = int(input('Mihin asti:'))
i=1
s=1
st = 'Laskettiin 1'

while s<n:
    i += 1
    s += i
    st += f' + {i}'

st += f' = {s}'

print(st)
