words = []

w = input('sana:')

while (w in words) == False:
  words.append(w)
  w = input('sana:')

print(f'Annoit {len(words)} eri sanaa')