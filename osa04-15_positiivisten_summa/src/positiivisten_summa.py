def positiivisten_summa(l: list) -> int:
  summ = 0

  for n in l:
    if int(n) > 0:
      summ += n

  return summ
