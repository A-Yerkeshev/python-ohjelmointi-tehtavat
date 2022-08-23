name = input('Kenelle teos omistetaan:')
destination = input('Mihin kirjoitetaan:')

with open(destination, 'w') as file:
  file.write(f'Hei {name}, toivomme viihtyisiä hetkiä python-kurssimateriaalin parissa! Terveisin mooc.fi-tiimi')
