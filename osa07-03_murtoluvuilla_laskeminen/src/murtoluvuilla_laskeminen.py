from fractions import Fraction

def jaa_palasiksi(p_num: int) -> list:
  result = []
  for i in range(0, p_num):
    result.append(Fraction(1, p_num))
  return result