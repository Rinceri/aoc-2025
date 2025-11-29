import requests
from getpass import getpass

url = input("URL for input: ")
session_id = getpass("Session ID (get it from Dev console > Application > Storage > Cookies): ")

cookies = {'session': session_id}
page = requests.get(url, cookies=cookies)

aoc_input = page.text

print(aoc_input)