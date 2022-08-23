import string

def vaihda_koko(s: str) -> str:
  res = ''

  for c in s:
    if c.isupper():
      res += c.lower()
    elif c.islower():
      res += c.upper()
    else:
      res += c

  return res

def puolita(s: str) -> tuple:
  mid = len(s)//2
  return (s[:mid], s[mid:])

def poista_erikoismerkit(s: str) -> str:
  res = ''
  allowed = string.ascii_letters + string.digits + 'ÄäÖöÅå '

  for c in s:
    if c in allowed:
      res += c

  return res