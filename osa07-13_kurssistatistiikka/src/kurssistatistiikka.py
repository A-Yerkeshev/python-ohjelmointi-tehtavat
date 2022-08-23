import urllib.request
import json
import certifi
import math

def get_courses() -> list:
  url = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
  req = urllib.request.urlopen(url, cafile=certifi.where())

  data = req.read()
  return json.loads(data)

def hae_kaikki() -> list:
  res = []
  courses = get_courses()

  for course in courses:
    if course['enabled']:
      res.append((course['fullName'], course['name'], course['year'], sum(course['exercises'])))

  return res

def hae_kurssi(c_name: str) -> dict:
  url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{c_name}/stats"
  req = urllib.request.urlopen(url, cafile=certifi.where())
  course = json.loads(req.read())

  max_students = 0
  total_hours = 0
  total_ex = 0

  for i, week in course.items():
    if week['students'] > max_students:
      max_students = week['students']
    total_hours += week['hour_total']
    total_ex += week['exercise_total']

  return {
    'viikkoja': len(course),
    'opiskelijoita': max_students,
    'tunteja': total_hours,
    'tunteja_keskimaarin': math.trunc(total_hours/max_students),
    'tehtavia': total_ex,
    'tehtavia_keskimaarin': math.trunc(total_ex/max_students)
  }
