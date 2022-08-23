from random import randint

def lottonumerot(size: int, bot: int, top: int) -> list:
  result = []
  while len(result) < size:
    num = randint(bot, top)
    if num not in result:
      result.append(num)
  return sorted(result)