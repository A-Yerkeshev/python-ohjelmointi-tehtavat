st = input('Sana:')

wrapper = '*'*30
sl = (28-len(st))//2
first_ws = ' '*sl
sl = 28-len(first_ws)-len(st)
second_ws = ' '*sl

mid = '*' + first_ws + st + second_ws + '*'

print(wrapper)
print(mid)
print(wrapper)
