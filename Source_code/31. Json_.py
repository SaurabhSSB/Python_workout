# JavaScript Object Notation: Data exchange format
student= {}
student["Anand"]= {
    "roll_no": 1,
    "gender": "male",
    "age": 22
}
student["Bhawandar"]= {
    "roll_no": 2,
    "gender": "male",
    "age": 23
}

import json
json_1= json.dumps(student)
print(json_1)

with open("Real.txt", "w") as f:
    f.write(json_1)

with open("Real.txt", "r") as g:
    x= g.read()
print(x)
entry= json.loads(x)
print(type(entry))
print(entry["Anand"])
print(entry["Bhawandar"]["age"])

for data in entry:
    print(f"{data}-> {entry[data]}")