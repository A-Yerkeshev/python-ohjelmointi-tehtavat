def vaihteluvali(a: list):
    return max(a) - min(a)

if __name__ == "__main__":
    lista = [3, 6, -4]
    tulos = vaihteluvali(lista)
    print(tulos)