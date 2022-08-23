def viiva(l, st):
    if len(st) == 0:
        st = '*'

    print(str(st[0])*int(l))

def kuvio(w, tc, h, sc):
    i = 0
    while i<=w:
        viiva(i, tc)
        i += 1

    i = 0
    while i<h:
        viiva(w, sc)
        i += 1

if __name__ == "__main__":
    kuvio(5, "X", 3, "*")
