def shakkilauta(size):
    rows=1
    while rows<=size:
        # Determine first character depending on row's parity
        if rows % 2 == 0:
            row = '01'*(size//2+1)
        else:
            row = '10'*(size//2+1)

        print(row[:size])
        rows += 1

if __name__ == "__main__":
    shakkilauta(5)
