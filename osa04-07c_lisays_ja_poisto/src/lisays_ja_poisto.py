a = []

print('Lista on nyt', a)
com = input('(l)isää, (p)oista vai e(x)it:')

while com != 'x':
  if com == 'l':
    a.append(len(a)+1)
  elif com == 'p':
    a.pop(-1)
  else:
    print('Unrecognized command.')
  print('Lista on nyt', a)
  com = input('(l)isää, (p)oista vai e(x)it:')

print('Moi!')