dictionary = []

with open('wordlist.txt') as textfile:
  for line in textfile:
    dictionary.append(line.strip())

inp = input('Write text:').split(' ')

result = ''
for word in inp:
  if word.lower() not in dictionary:
    result += f'*{word}* '
  else:
    result += word + ' '

print(result.strip())
