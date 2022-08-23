p = int(input('Anna pisteet [0-100]:'))

if p<0 or p>100:
    g='mahdotonta!'
elif 0 <= p < 50:
    g='hylätty'
elif 50 <= p < 60:
    g=1
elif 60 <= p < 70:
    g=2
elif 70 <= p < 80:
    g=3
elif 80 <= p < 90:
    g=4
elif 90 <= p <= 100:
    g=5

print('Arvosana:', g)
