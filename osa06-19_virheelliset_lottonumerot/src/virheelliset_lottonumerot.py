def suodata_virheelliset():
  with open('lottonumerot.csv') as source, open('korjatut_numerot.csv', 'w') as dest:
    for line in source:
      if validate_entry(line.strip()):
        dest.write(line)

def validate_entry(entry:str):
  parts = entry.split(';')
  week_num = parts[0].split(' ')[1]
  lotto_nums = parts[1].split(',')

  try:
    int(week_num)
  except ValueError:
    return False

  if len(lotto_nums) < 7:
    return False

  for num in lotto_nums:
    try:
      if lotto_nums.count(num) > 1:
        return False

      num = int(num)

      if num<1 or num>39:
        return False
    except ValueError:
      return False

  return True