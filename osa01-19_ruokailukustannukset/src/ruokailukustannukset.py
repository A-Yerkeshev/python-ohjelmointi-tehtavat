# Kirjoita ratkaisu tähän
kert = int(input('Montako kertaa viikossa syöt Unicafessa?'))
hinta = float(input('Unicafe-lounaan hinta?'))
muu = float(input('Paljonko käytät viikossa ruokaostoksiin?'))

viikossa = kert*hinta+muu

print('Kustannukset keskimäärin:')
print(f'Päivässä {viikossa/7} euroa')
print(f'Viikossa {viikossa} euroa')