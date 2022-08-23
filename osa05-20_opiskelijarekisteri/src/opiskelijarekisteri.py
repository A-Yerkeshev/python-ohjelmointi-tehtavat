def lisaa_opiskelija(record:dict, name:str):
  record[name] = []

def lisaa_suoritus(record:dict, name:str, course:tuple):
  # Check if course with this name is already present
  for i in range(len(record[name])):
    if record[name][i][0] == course[0]:
      if course[1] > record[name][i][1]:
        record[name][i] = course
      return

  # If execution gets here, it means course is not present yet
  if course[1] > 0:
    record[name].append(course)

def tulosta(record:dict, name:str):
  if name not in record:
    print('ei löytynyt ketään nimellä', name)
  else:
    print(f'{name}:')
    print(' ', end='')
    if len(record[name]) == 0:
      print('ei suorituksia')
    else:
      print(f'suorituksia {len(record[name])} kurssilta:')

      grades_sum = 0

      for course in record[name]:
        print('  ', end='')
        print(course[0], course[1])
        grades_sum += course[1]

      print(' ', end='')
      print('keskiarvo', grades_sum/len(record[name]))

def kooste(record:dict):
  total_stud = 0
  max_courses = ('', 0)
  best_grade = ('', 0)

  for stud, perf in record.items():
    total_stud += 1
    average = 0

    for course in perf:
      if len(perf) > max_courses[1]:
        max_courses = (stud, len(perf))
      average += course[1]
    average /= len(perf)

    if average > best_grade[1]:
      best_grade = (stud, average)

  print('opiskelijoita', total_stud)
  print('eniten suorituksia', max_courses[1], max_courses[0])
  print('paras keskiarvo', best_grade[1], best_grade[0])