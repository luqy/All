import requests
import binascii
import html
from urllib.parse import urlencode,quote,unquote
url="https://www.zhuishu5.com/?searchtype=articlename&searchkey="
value=u"圣墟"
key=urlencode({"searchkey":value})
print(html.escape(value))
key3=binascii.b2a_hex(u"圣墟".encode("gb2312"))
#key1=quote(key3)
print(key3)

