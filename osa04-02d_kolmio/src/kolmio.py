def viiva(l, st):
    if len(st) == 0:
        st = '*'

    print(str(st[0])*int(l))

def kolmio(koko):
    i = 0
    while i<=koko:
        viiva(i, "#")
        i += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kolmio(5)
