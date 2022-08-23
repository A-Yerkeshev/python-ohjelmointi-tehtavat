def eka_sana(str):
    arr = str.split(' ')
    return arr[0]

def toka_sana(str):
    arr = str.split(' ')
    return arr[1]

def vika_sana(str):
    arr = str.split(' ')
    return arr[-1]


if __name__ == "__main__":
    lause = "olipa kerran kauan sitten ohjelmoija"
    print(eka_sana(lause))
    print(toka_sana(lause))
    print(vika_sana(lause))