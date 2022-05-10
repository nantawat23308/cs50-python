names = []

with open("name.txt") as file:  #ไม่ต้องใส่ "r"ก็ได้ เพราะเป็น default
    for line in file:
        names.append(line.rstrip())  #append currrent line

for name in sorted(names, reverse = True):
    print(f"hello, {name}") 

    #ผ่านการ sort แล้ว