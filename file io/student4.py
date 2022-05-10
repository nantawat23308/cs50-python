import csv

students = [] 

with open("student.csv") as file:
    reader = csv.DicReader(file)
    for row in reader:
        students.append({"name": row["name"],"home": row["home"]})


for student in sorted(students, key = lambda student: student["name"] , reverse = True): 
    print(f"{student['name']} is in {student['home']}")  
    

