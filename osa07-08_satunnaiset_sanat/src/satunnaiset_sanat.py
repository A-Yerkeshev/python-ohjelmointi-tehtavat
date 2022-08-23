from random import sample

def sanat(n: int, start: str) -> list:
  words = []

  with open('sanat.txt') as file:
    for line in file:
      if line.startswith(start):
        words.append(line.strip())

  return sample(words, n)
