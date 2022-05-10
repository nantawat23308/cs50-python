students = [] 

with open("name.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        
        #student = {} #create dictionary
        #student["name"] = name
        #student["house"] = house

        students.append(student)
    
def get_name(student):
    return student["name"]


def get_house(student):
    return student["house"]

for student in sorted(students, key = get_house, reverse = True):  #ใช้ key ในการ sorted ซึ่งคือ ฟังชัน get_name หรือ lambda student: student["name"]
    print(f"{student['name']} is in {student['house']}")  
    #ใน dictionary เรียกชือ ถ้าเป็น ใน list จะเรียก [0],[1]
    #ใช้ ' แยกกับ " กับข้างนอก


