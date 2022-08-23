dictionary = {}
print('1 - Lisää sana, 2 - Hae sanaa, 3 - Poistu')
command = input('Valinta:').strip()

while command != '3':
  if command == '1':
    fin = input('Anna sana suomeksi:').strip()
    en = input('Anna sana englanniksi:').strip()

    with open('sanakirja.txt', 'a') as file:
      file.write(f'{fin} - {en}\n')

    print('Sanapari lisätty')
  elif command == '2':
    search = input('Anna sana:').strip()

    with open('sanakirja.txt') as file:
      for line in file:
        if search in line:
          print(line.strip())
  else:
    print('Unrecognized command')

  print('1 - Lisää sana, 2 - Hae sanaa, 3 - Poistu')
  command = input('Valinta:').strip()

print('Moi!')
