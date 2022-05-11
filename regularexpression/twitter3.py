import re

url = input("URL: ").strip()


if matches := re.search("^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):  #ใช้ (?:... ) เพื่อบอกว่าไม่นับ 
    print(f"Username:", matches.group(1))