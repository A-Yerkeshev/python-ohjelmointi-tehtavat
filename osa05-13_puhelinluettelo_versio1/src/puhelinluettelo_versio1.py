phone_nums = {}

command = int(input('komento (1 hae, 2 lisää, 3 lopeta):'))

while command != 3:
  name = input('nimi:')

  if command == 1:
    if name in phone_nums:
      print(phone_nums[name])
    else:
      print('ei numeroa')
  elif command == 2:
    phone_nums[name] = input('numero:')
    print('ok!')
  else:
    print('Unrecognized command')

  command = int(input('komento (1 hae, 2 lisää, 3 lopeta):'))

print('lopetetaan...')
