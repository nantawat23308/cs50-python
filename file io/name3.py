with open("name.txt", "r") as file:
    for line in file:
        print("hello," , line.rstrip())
        



"""   lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())  #ใช้ end = "" ก็ได้

"""