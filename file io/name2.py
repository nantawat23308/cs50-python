name = input("what is your name?:")


    #ใช้ read หรือ write information w ใช้เขียน replace อันเดิม 
    #เราสามารถใช้ with แทน file.close
with open("name.txt", "a") as file:
    file.write(f"{name}\n")

#file.close() #ใช้ในการ save 
    