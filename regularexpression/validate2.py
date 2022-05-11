import re

email = input("what is your email?: ").strip().lower() #แปลงเป็นพิมพ์เล็ก

"""if re.search("^[a-zA-Z0-9_]+@+[^@]\.edu$", email):
"""  #[^@] คือ ยกเว้น @  และ [a-zA-Z0-9_] บอกว่าใช้ตัวอะไรได้ใน set นี้

'''if re.search("^(\w|\s)+@+\w\.(edu|com|gov|org)$", email, re.IGNORECASE): 
'''  #\w คือ character ใช้ re.IGNORECASE ในการไม่สนใจ ว่าตัวใหญ่หรือตัวเล็ก

if re.search("^\w+@(\w\.)?\w+\.edu$", email, re.IGNORECASE): #ใช้ ? ในการบอกสิ่งที่อยู๋ในวงเล็บว่ามีหรือไม่มีก็ได้
    print("Valid")
else:
    print("Invalid")