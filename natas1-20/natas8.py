import base64
from binascii import unhexlify
str = '3d3d516343746d4d6d6c315669563362'
str = unhexlify(str)

str = str[::-1]


str = base64.b64decode(str)


print(str)