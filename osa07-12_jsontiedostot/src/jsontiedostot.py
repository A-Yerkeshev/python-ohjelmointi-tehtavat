import json

def tulosta_henkilot(filename: str):
  with open(filename) as file:
    data = file.read()
  students = json.loads(data)

  for student in students:
    print(f"{student['nimi']} {student['ika']} vuotta ({', '.join(student['harrastukset'])})")