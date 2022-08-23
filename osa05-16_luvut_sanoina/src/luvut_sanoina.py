def lukukirja() -> dict:
  result = {}
  singulars = ['nolla',
  'yksi',
  'kaksi',
  'kolme',
  'neljä',
  'viisi',
  'kuusi',
  'seitsemän',
  'kahdeksan',
  'yhdeksän']

  for i in range(0, 10):
    result[i] = singulars[i]
  result[10] = 'kymmenen'

  for i in range(11, 20):
    result[i] = singulars[i-10] + 'toista'

  for i in range(20, 100):
    result[i] = singulars[i//10] + 'kymmentä'
    if i%10 != 0:
      result[i] += singulars[i%10]

  return result