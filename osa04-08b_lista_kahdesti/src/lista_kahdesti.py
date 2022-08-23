a = []

n = int(input('Anna luku:'))

while n != 0:
  a.append(n)
  print('Lista:', a)
  print('Järjestettynä:', sorted(a))

  n = int(input('Anna luku:'))

print('Moi!')