def samat(str, i1, i2):
    if i1>len(str)-1 or i2>len(str)-1:
        return False

    if str[i1] == str[i2]:
        return True
    else:
        return False


if __name__ == "__main__":
    print(samat("koodari", 1, 2))