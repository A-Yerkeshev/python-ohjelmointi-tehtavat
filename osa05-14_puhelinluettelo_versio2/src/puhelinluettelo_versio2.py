phone_nums = {}

command = int(input('komento (1 hae, 2 lisää, 3 lopeta):'))

while command != 3:
  name = input('nimi:')

  if command == 1:
    if name in phone_nums:
      for num in phone_nums[name]:
        print(num)
    else:
      print('ei numeroa')
  elif command == 2:
    if name in phone_nums:
      phone_nums[name].append(input('numero:'))
    else:
      phone_nums[name] = [input('numero:')]
    print('ok!')
  else:
    print('Unrecognized command')

  command = int(input('komento (1 hae, 2 lisää, 3 lopeta):'))

print('lopetetaan...')
