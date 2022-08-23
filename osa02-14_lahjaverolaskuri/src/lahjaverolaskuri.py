amount = int(input('Lahjan suuruus? '))

if amount < 5000:
    tax = 0
elif amount < 25000:
    tax = (100 + (amount-5000) * 0.08)
elif amount < 55000:
    tax = (1700 + (amount-25000) * 0.1)
elif amount < 200000:
    tax = (4700 + (amount-55000) * 0.12)
elif amount < 1000000:
    tax = (22100 + (amount-200000) * 0.15)
else:
    tax = (142100 + (amount-1000000) * 0.17)

if tax==0:
    print('Ei veroa!')
else:
    print(f'Vero: {tax} euroa')
