def palindromi(s: str):
  if s == s[::-1]:
    return True
  else:
    return False

s = input('Anna palindromi:')

while palindromi(s) == False:
  print('ei ollut palindromi')
  s = input('Anna palindromi:')

print(s, 'on palindromi!')
