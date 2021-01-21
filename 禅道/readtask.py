from lxml import html
import re
import pandas as pd
etree=html.etree
path=r"F:\All\task.html"

with open(path,encoding="utf-8")as f:
    h=f.read()
df=pd.read_html(h)[0]
#print(y)
#print(df["所属项目"].to_list())
#print(df[df["状态"].isin(['已完成'])])
print(df[(df['所属项目']=='自助打印维护 2020')&(df['状态']=='已完成')])
# for i in table:
#     print(i)
# path2=r'F:\All\pyecharts\123.csv'
# csv=pd.read_csv(path2)
# print(type(csv))