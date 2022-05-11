import re

name = input("what is your name?: ").strip()



if matches := re.search("^(.+), *(.+)$", name):

   
    name = matches.group(2) + " " + matches.group(2)

print(f"helo, {name}")