def viiva(l, st):
    if len(st) == 0:
        st = '*'

    print(str(st[0])*int(l))

if __name__ == "__main__":
    viiva(5, "")
