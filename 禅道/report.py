import requests
import re
url='http://eword.66ip.net:8086/zentao/release-edit-128.html'
#url='http://eword.66ip.net:8086/zentao/bug-browse-3-0-all.html'
# header1={
#     "cookie":"lang=zh-cn; device=desktop; theme=default; keepLogin=on; za=lqy; zp=de354461b230d3f02408b03e47cefe9ff5923f5e; preBranch=0; preProductID=3; bugModule=0; lastProduct=3; qaBugOrder=id_desc; windowHeight=722; windowWidth=812; zentaosid=0kgp40ghd6huom31gfu937t3b7"
# }
header={
'Cookie': 'lang=zh-cn; device=desktop; theme=default; keepLogin=on; za=lqy; preBranch=0; preProductID=3; selfClose=0; lastProject=50; preProjectID=50; pagerProjectTesttask=100; lastProduct=3; zp=21cdd30d4f702a9868ffa12df27b5f257f9d4aab; qaBugOrder=id_desc; windowWidth=1422; windowHeight=600; zentaosid=gn0hp45r58fb8usbf41q0qjr73'
}
response=requests.request(method="get",url=url,headers=header)
# with open("F:\All\cs.html",encoding="utf-8") as f:
#     h=f.read()
print(response.text)
#print(h)
fre=re.search('var kuid =(.*)',response.text).group(0)
print(fre)
h=re.findall('var kuid =..(\w+)',response.text)[0]
header={
    "cookie":"lang=zh-cn; device=desktop; theme=default; keepLogin=on; za=lqy; zp=de354461b230d3f02408b03e47cefe9ff5923f5e; preBranch=0; preProductID=3; bugModule=0; lastProduct=3; qaBugOrder=id_desc; windowHeight=722; windowWidth=812; zentaosid=0kgp40ghd6huom31gfu937t3b7",
    "Content-Type":"multipart/form-data; boundary=----WebKitFormBoundaryKtd7aulobsna2TCE",
}
