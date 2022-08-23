import string

def jaa_merkkeihin(s: str) -> tuple:
  en_chars = ''
  punct = ''
  other = ''
  for c in s:
    if c in string.ascii_letters:
      en_chars += c
    elif c in string.punctuation:
      punct += c
    else:
      other += c
  return (en_chars, punct, other)