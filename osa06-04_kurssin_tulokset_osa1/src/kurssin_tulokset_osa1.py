if True:
    # tänne ei tulla
    studfilename = input("Opiskelijatiedot: ")
    taskfilename = input("Tehtävätiedot: ")
else:
    # kovakoodatut syötteet
    studfilename = "opiskelijat1.csv"
    taskfilename = "tehtavat1.csv"

data = {} # studnumber: {name: (first_name, last_name), grades: []}

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

def print_results():
  for stud_id, stud_data in data.items():
    print(stud_data['name'][0], stud_data['name'][1], sum(stud_data['tasks']))

read_students()
read_tasks()
print_results()