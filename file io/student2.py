students = [] 

with open("name.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students): 
    print(student)

    #อ่านชื่อใน file แล้ว sorted แล้วจึงปริ้นค่า
    