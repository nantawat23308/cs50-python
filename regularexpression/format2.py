import re

name = input("what is your name?: ").strip()

matches = re.search("^(.+), *(.+)$", name)

if matches:
    first, last = matchs.groups()

    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"
    #name = matches.group(2) + " " + matches.group(2)

print(f"helo, {name}")