# Korjaa ohjelma
pisteet = int(input("Kuinka paljon pisteitä? "))

if pisteet < 100:
    bonus = 1.1
    print("Sait 10 % bonusta")

if pisteet >= 100:
    bonus = 1.15
    print("Sait 15 % bonusta")

pisteet *= bonus

print("Pisteitä on nyt", pisteet)
