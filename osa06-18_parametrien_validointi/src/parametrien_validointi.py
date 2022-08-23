def uusi_henkilo(name: str, age: int) -> tuple:
  if name == '' or len(name.split(' ')) < 2 or len(name) > 40:
    raise ValueError('Invalid name')
  elif age < 0 or age > 150:
    raise ValueError('Invalid age')
  return (name, age)