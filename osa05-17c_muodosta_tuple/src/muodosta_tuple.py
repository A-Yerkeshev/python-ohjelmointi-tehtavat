def tee_tuple(x: int, y: int, z: int) -> tuple:
  return (min([x, y, z]), max([x, y, z]), sum([x, y, z]))