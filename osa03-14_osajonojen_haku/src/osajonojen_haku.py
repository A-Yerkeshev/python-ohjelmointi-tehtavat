st = input('Sana:')
c = input('Merkki:')

i = st.find(c)
while i != -1:
    res = (st[i:i+3])

    if len(res) >= 3:
        print(res)

    st = st[i+1:]
    i = st.find(c)

