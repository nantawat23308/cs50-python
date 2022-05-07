#except value error 
#use try and except to except value error

#NameError error ใน state ment error เลยทำให้ ไม่มี formate ของ x เลย print x ไม้่ได้ แก้โดยใช้ else

#ใช้ loop และ break ใน การรับ input เรื่อยกว่าจะไม่ value error
while True:

    try:
        x = int(input("what is x: "))
    
    except ValueError:
        print("x is not integer")
    
    else:
        break
        

print(f" x is {x}")
