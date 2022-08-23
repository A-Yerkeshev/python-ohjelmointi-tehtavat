w1 = input('Anna 1. sana:')
w2 = input('Anna 2. sana:')

if w1>w2:
    print(f'{w1} on aakkosjärjestyksessä viimeinen.')
elif w2>w1:
    print(f'{w2} on aakkosjärjestyksessä viimeinen.')
elif w1 == w2:
    print('Annoit saman sanan kahdesti.')

