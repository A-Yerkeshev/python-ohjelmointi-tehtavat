from difflib import get_close_matches

dictionary = []
suggestions = {}

with open('wordlist.txt') as textfile:
  for line in textfile:
    dictionary.append(line.strip())

inp = input('Write text:').split(' ')

result = ''
for word in inp:
  if word.lower() not in dictionary:
    result += f'*{word}* '
    suggestions[word] = get_close_matches(word, dictionary)
  else:
    result += word + ' '

print(result.strip())
print('korjausehdotukset:')
for word, fixes in suggestions.items():
  print(word + ': ' + ', '.join(fixes))
