email = input("what is your email?: ").strip()

username, domain = email.split("@") #ใช้ @ ในการ split 2 ข้างแล้วเก็บใน username และ domain

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")