import string

def main():
  letters = string.ascii_uppercase
  depth = int(input('Kerrokset:'))

  for i in range(0, depth):
    s = ''

    for j in range(1, i+1):
      s += letters[depth-j]

    s += letters[depth-1-i-0]*(depth*2-(1+i*2))

    for j in range(i, 0, -1):
      s += letters[depth-j]

    print(s)

  for i in range(depth-2, -1, -1):
    s = ''

    for j in range(1, i+1):
      s += letters[depth-j]

    s += letters[depth-1-i-0]*(depth*2-(1+i*2))

    for j in range(i, 0, -1):
      s += letters[depth-j]

    print(s)
main()
