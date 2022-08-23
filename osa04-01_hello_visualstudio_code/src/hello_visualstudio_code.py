editori = input("editori: ").lower()

while editori != 'visual studio code':
  if editori == "word" or editori == "notepad":
    print("surkea")
  else:
    print('ei ole hyvä')
  editori = input("editori: ").lower()

print('loistava valinta!')
