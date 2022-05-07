#except value error 
#use try and except to except value error

#NameError error ใน state ment error เลยทำให้ ไม่มี formate ของ x เลย print x ไม้่ได้ แก้โดยใช้ else

#ใช้ loop และ break ใน การรับ input เรื่อยกว่าจะไม่ value error


def main():
    x = get_int("what is x?:")
    print(f"x is {x}")


def get_int(prompt):
    while True:

        try:
            x = int(input(prompt))
    
        except ValueError:
            print("x is not integer")

        else:
            #break #ใช้ ออกจาก loop
            return x #ได้ x และ ออกจาก loop
        #retern x
            #pass ใช้ ผ่าน error ไปเลย แล้วรับค่าใหม่
main()