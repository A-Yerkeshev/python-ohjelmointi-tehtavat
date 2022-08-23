import csv
from datetime import datetime

def viralliset_pisteet() -> dict:
  test_starts = {}
  test_results = {}
  total_scores = {}

  with open('tentin_aloitus.csv') as file:
    for line in csv.reader(file, delimiter=";"):
      test_starts[line[0]] = datetime.strptime(line[1], "%H:%M")

  with open('palautus.csv') as file:
    for line in csv.reader(file, delimiter=";"):
      name = line[0]
      task_id = line[1]
      points = line[2]

      # Reject if time is greater than 3 hours
      if (datetime.strptime(line[3], "%H:%M") - test_starts[name]).seconds/3600 <= 3:
        # Check if student has record
        if name in test_results and test_results[name]:
          # Assign value if this task was not submitted before, or new score is higher
          if task_id not in test_results[name] or points > test_results[name][task_id]:
            test_results[name][task_id] = points
        else:
          test_results[name] = {task_id: points}

  for name, scores in test_results.items():
    summ = 0
    for task, score in scores.items():
      summ += int(score)

    total_scores[name] = summ

  return total_scores