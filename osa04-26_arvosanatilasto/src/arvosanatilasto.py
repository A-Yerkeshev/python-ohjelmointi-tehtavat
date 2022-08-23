def main():
  user_input = receive_input()
  tp = user_input[0]
  en = user_input[1]

  # Convert number of excercizes to excercize points
  ep = []
  for ex in en:
    ep.append(ex//10)

  # Calculate grades
  points = []
  grades = []
  for i in range(len(tp)):
    point = tp[i]+ep[i]

    if tp[i] < 10:
      grades.append(0)
    else:
      grade = 0

      # increment grade on 15, 18, 21 and 24
      for i in range(15, 25, 3):
        if point >= i:
          grade += 1
        else:
          break
      if grade == 4 and point >= 28:
        grade += 1

      grades.append(grade)
    points.append(point)

  print_results(sum(points)/len(points), grades)

def receive_input():
  tp = []
  ep = []

  inp = input('Koepisteet ja harjoitusten määrä:')

  while inp != '':
    numstrings = inp.split(' ')
    tp.append(int(numstrings[0]))
    ep.append(int(numstrings[1]))

    inp = input('Koepisteet ja harjoitusten määrä:')

  return [tp, ep]

def print_results(avr, grades):
  print('Tilasto:')
  print('Pisteiden keskiarvo:', avr)
  passrate = (len(grades)-grades.count(0))/len(grades)*100
  print('Hyväksymisprosentti:', f'{passrate:.1f}')
  print('Arvosanajakauma:')
  for i in range (5,-1,-1):
    print(f'{i}:', '*'*grades.count(i))
main()