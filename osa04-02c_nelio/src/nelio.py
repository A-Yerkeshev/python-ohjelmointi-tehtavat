def viiva(l, st):
    if len(st) == 0:
        st = '*'

    print(str(st[0])*int(l))

def nelio(koko, merkki):
    i = 0
    while i<koko:
        viiva(koko, merkki)
        i += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    nelio(5, "o")
