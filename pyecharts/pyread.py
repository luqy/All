import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line,Page
import os
path=r"F:\All\pyecharts\csv"
page=Page()
line1=Line()
line2=Line()
line3=Line()
line4=Line()
name=["pid","pidname","pidtime","cpu%","menmory%","menmorySize"]
csv_list=os.listdir(path)
# print(os.path.getctime(path))
# newctime=os.stat(os.path.join(path,csv_list[0])).st_ctime
# id=0
# for i in range(1,len(csv_list)):
#     print(i)
#     oldtime=os.stat(os.path.join(path,csv_list[i])).st_ctime
#     if newctime<oldtime:
#         newctime=newctime
#         id=0
#     else:
#         newctime=oldtime
#         id=i
# print(newctime)
# print(csv_list[id])
for i in range(len(csv_list)):
    df=pd.read_csv(os.path.join(path,csv_list[i]),names=name)
    #print(type(df))
    cpu=df["cpu%"].to_list()
    men=df["menmory%"].to_list()
    mens=df["menmorySize"].to_list()
    pidtime=pd.read_csv(os.path.join(path,csv_list[0]),names=name)["pidtime"].to_list()
    print("CPU",cpu)
    print("men",men)
    print("mens",mens)
    print("pidtime",pidtime)
    line1.add_xaxis(pidtime)
    line1.add_yaxis(csv_list[i],cpu)
    line2.add_xaxis(pidtime)
    line2.add_yaxis(csv_list[i],men)
    line3.add_xaxis(pidtime)
    line3.add_yaxis(csv_list[i],mens)
page.add(line1)
page.add(line2)
page.add(line3)
page.render()