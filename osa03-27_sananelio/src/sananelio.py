def nelio(st, size):
    i=0
    while i<size:
        p = st[i*size%len(st):]

        while len(p) < size:
            p += st
        p = p[:size]
        print(p)

        i += 1

if __name__ == "__main__":
    nelio("aybabtu", 5)