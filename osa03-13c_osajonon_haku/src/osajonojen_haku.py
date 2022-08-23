st = input('Sana:')
c = input('Merkki:')

i = st.find(c)
res = (st[i:i+3])

if len(res) >= 3:
    print(res)
