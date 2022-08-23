def tallenna_henkilo(pers: tuple):
  with open('henkilot.csv', 'a') as file:
    file.write(f'{pers[0]};{pers[1]};{pers[2]}')