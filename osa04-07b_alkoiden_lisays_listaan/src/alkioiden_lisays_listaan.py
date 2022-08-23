lng = int(input('Kuinka monta lukua:'))
a = []

while len(a)<lng:
  a.append(int(input(f'Anna luku {len(a)+1}')))

print(a)