if True:
    # tänne ei tulla
    studfilename = input("Opiskelijatiedot: ")
    taskfilename = input("Tehtävätiedot: ")
    testfilename = input("Koepisteet: ")
else:
    # kovakoodatut syötteet
    studfilename = "opiskelijat1.csv"
    taskfilename = "tehtavat1.csv"
    testfilename = "koepisteet1.csv"

data = {} # studnumber: {name: (first_name, last_name), tasks: [], test_grades: []}

def read_students():
  with open(studfilename.strip()) as csvfile:
    for line in csvfile:
      parts = line.strip().split(';')

      stud_id = parts[0]
      if stud_id != 'opnro':
        if not stud_id in data or not data[stud_id]:
          data[stud_id] = {'name': (parts[1], parts[2])}
        else:
          data[stud_id]['name'] = (parts[1], parts[2])

def read_tasks():
  with open(taskfilename.strip()) as csvfile:
    for line in csvfile:
      parts = line.strip().split(';')

      stud_id = parts[0]
      if stud_id != 'opnro':
        tasks = []
        for s in parts[1:]:
          tasks.append(int(s))

        if not stud_id in data or not data[stud_id]:
          data[stud_id] = {'tasks': tasks}
        else:
          data[stud_id]['tasks'] = tasks

def read_test_scores():
  with open(testfilename.strip()) as csvfile:
    for line in csvfile:
      parts = line.strip().split(';')

      stud_id = parts[0]
      if stud_id != 'opnro':
        grades = []
        for s in parts[1:]:
          grades.append(int(s))

        if not stud_id in data or not data[stud_id]:
          data[stud_id] = {'test_grades': grades}
        else:
          data[stud_id]['test_grades'] = grades

def calc_grade(total_points:int) -> int:
  thresholds = [15, 18, 21, 24, 28]
  grade = 0

  for i in range(0, int(total_points)+1):
    if i in thresholds:
      grade += 1

  return grade

def print_results():
  print(f"{'nimi':30}{'teht_lkm':10}{'teht_pist':10}{'koe_pist':10}{'yht_pist':10}{'arvosana':10}")

  for stud_id, stud_data in data.items():
    name = stud_data['name'][0] + ' ' + stud_data['name'][1]
    tasks_num = sum(stud_data['tasks'])
    task_points = int(tasks_num/0.4//10)
    test_points = sum(stud_data['test_grades'])
    total_points = task_points + test_points
    grade = calc_grade(total_points)

    print(f"{name:30}{tasks_num:<10}{task_points:<10}{test_points:<10}{total_points:<10}{grade:<10}")

read_students()
read_tasks()
read_test_scores()
print_results()
