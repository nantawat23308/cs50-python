name = input("what is your name?: ").strip()

if "," in name:
    last, first = name.split(", ?") #ข้างซ้าย ? จะมีหรือไม่มีก็ได้
    name = f"{first} {last}"
print(f"hello,{name}")