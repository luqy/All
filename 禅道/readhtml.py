from lxml import html
import re
etree=html.etree
path="F:\All\cs.html"

with open(path,encoding="utf-8")as f:
    h=f.read()
b=re.findall("<option value='(.*?)' title='(.*?)' data-keys='.*?'>(.*?)</option>",h)
# for i in range(len(b)):
#     if "QZ_V1.0.0.5" in b[i]:
#         print(i)
print(b)

