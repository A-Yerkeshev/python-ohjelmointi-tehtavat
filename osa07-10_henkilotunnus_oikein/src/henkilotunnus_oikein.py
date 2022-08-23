from datetime import datetime

def onko_validi(hetu: str) -> bool:
  if len(hetu) != 11:
    return False

  b_date_str = hetu[:6]
  p_code = hetu[7:-1]
  day = int(b_date_str[:2])
  month = int(b_date_str[2:4])

  # Validate century mark
  if hetu[6] == '+':
    year = int('18' + b_date_str[4:])
  elif hetu[6] == '-':
    year = int('19' + b_date_str[4:])
  elif hetu[6] == 'A':
    year = int('20' + b_date_str[4:])
  else:
    return False

  # Validate birthday
  try:
    birth_date = datetime(year, month, day)
  except ValueError:
    return False

  # Validate last char
  if hetu[-1] != '0123456789ABCDEFHJKLMNPRSTUVWXY'[int(b_date_str + p_code)%31]:
    return False

  return True

