# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(l, st):
    if len(st) == 0:
        st = '*'

    print(str(st[0])*int(l))

def risulaatikko(korkeus):
    i = 0
    while i<korkeus:
        viiva(10, "#")
        i += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risulaatikko(5)
