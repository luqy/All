import requests
from lxml import html
from zhuishu.config import url
import re
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
            'Content-Type': 'text/html'
           }
etree=html.etree
res=requests.request(method="GET",url=url,headers=headers)
res_tree=etree.HTML(res.content)
#result=etree.tostring(tree)
text=res_tree.xpath('//div//nav[@id="nav-header"]//li/a[@title="小说搜索"]/@href')
search_url=url+text[0]
search_res=requests.request(method="get",url=search_url,headers=headers)
search_tree=etree.HTML(search_res.content)
hex_url="https://www.107000.com/T-HexApi"
date={
    "t":"jiaG",
    "v":"圣墟",
    "p":True
}
hex_res=requests.request(method="post",url=hex_url,data=date)
#print(hex_res.content)
par={
    "searchtype":"articlename",
    "searchkey":hex_res.content.decode("utf-8")
}
#print(par)
s_url=search_url+"?searchtype=articlename&searchkey="+hex_res.content.decode("utf-8")
print(s_url)
s=requests.request(method="get",url=s_url,data=par, headers=headers)
# print(s.headers)
# print(s.url)
# print(s.text)
test_tree=etree.HTML(s.content)
s_test=test_tree.xpath('//div[@class="panel panel-default"]//div[@class="col-md-10"]/h1/a/@href')
#print(s_test[0])
#print(len(s_test))
for i in range(1):
    #print(s_test[i])
    html_test=requests.request(method="get",url=s_test[i],headers=headers)
    html_etree=etree.HTML(html_test.content)
    #text_url=html_etree.xpath('//div[@id="list-chapterAll"]/dl/dd[@class="col-md-3"]/a/@href|//div[@id="list-chapterAll"]/dl/dd[@class="col-md-3"]/a/@title')
    text_1=html_etree.xpath('//div[@id="list-chapterAll"]/dl/dd[@class="col-md-3"]/a')
    print(text_1[0].attrib.get('href'),text_1[0].text)
    for x in range(len(text_1)):
        print(x)
        print(text_1[x].attrib.get('href'), text_1[x].text)
        text_text=requests.request(method="get",url=url+text_1[x].attrib.get('href'),headers=headers)
        text_text_tree=etree.HTML(text_text.content)
        page=text_text_tree.xpath('//div[@id="content"]//h1[@class="readTitle"]/small/text()')
        print(page)
        print(type(re.findall("\d+",page[0])[1]))
        content=text_text_tree.xpath('//div[@id="htmlContent"]/text()')
        path1=text_1[x].attrib.get('href').rsplit('.')[0]
        print(path1)
        for z in range(1,int(re.findall("\d+",page[0])[1])):
            page_url=url+path1+'_'+str(z+1)+'.html'
            page_next=requests.request(method="get",url=page_url,headers=headers)
            page_next_tree=etree.HTML(page_next.content)
            content_next=page_next_tree.xpath('//div[@id="htmlContent"]/text()')
            content=content+content_next
        newfile='F:\All\zhuishu\圣墟'
        with (open(newfile + '/' + text_1[x].text, 'wb')) as f:
            #f.write(content)
            for y in range(len(content)):
                f.write(content[y].encode())


