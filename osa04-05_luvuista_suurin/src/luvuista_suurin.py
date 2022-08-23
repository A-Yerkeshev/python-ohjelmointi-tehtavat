def luvuista_suurin(n1, n2, n3):
    max = n1
    nums = [n1, n2, n3]

    for n in nums:
        if n>max:
            max = n

    return max


if __name__ == "__main__":
    suurin = luvuista_suurin(5, 4, 8)
    print(suurin)