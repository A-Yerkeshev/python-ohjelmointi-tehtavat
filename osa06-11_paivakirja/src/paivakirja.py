print('1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta')
command = input('Valinta:')

while command != '0':
  if command == '1':
    entry = input('Anna merkintä:')

    with open('paivakirja.txt', 'a') as file:
      file.write(entry + '\n')

    print('Päiväkirja tallennettu')
    print()
  elif command == '2':
    print('Merkinnät:')

    with open('paivakirja.txt') as file:
      for line in file:
        print(line)
  else:
    print('Unrecognized command')
  print('1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta')
  command = input('Valinta:')

print('Heippa!')