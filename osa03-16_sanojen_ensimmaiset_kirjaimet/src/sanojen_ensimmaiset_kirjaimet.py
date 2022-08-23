st = input('Anna lause:')

print(st[0])

i = st.find(' ')
while i != -1:
    st = st[i+1:]
    print(st[0])
    i = st.find(' ')
