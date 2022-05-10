with open("name.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",") #สามารถใช้ 2 parameter มารับได้
        print(f"{name} is in {house}")




"""
        row = line.rstrip().split(",") #ใช้ , ในการ split 
        print(f"{row[0]} is in {row[1]}")

"""
        
