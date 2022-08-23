def joulukuusi(h):
    print('joulukuusi!')

    i=1
    while i<=h:
        print(' '*(h-i) + '*'*i + '*'*(i-1))
        i += 1
    print(' '*(h-1) + '*')

if __name__ == "__main__":
    joulukuusi(5)