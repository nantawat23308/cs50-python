import re

url = input("URL: ").strip()

"""
username = url.removeprefix("https://twitter.com/")
"""
username = re.sub("^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")

