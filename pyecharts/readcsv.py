from pyecharts.charts import Line,Timeline,Page
import pandas as pd
from pyecharts.options import TitleOpts,InitOpts
# line=Line("折线图")
# attr=['7-1','7-2','7-3','7-4','7-5']
# line.add("最高在线",attr,[725,284,613,852,679],mark_point=["max","min"],mark_line=["average"])
# line.add("平均在线",attr,[30,20,40,80,70],legend_pos="20%")
# line.render('line.html') #我电脑中默认保存位置为‘C:\Users\gui\’
df=pd.read_csv(r"F:\All\pyecharts\csv\TomTaw.eWord.AutomaticTeller.exe_1188.csv")
print(len(df))
#print(df["pidtime"].tolist())
labels = list(df.values)
print(len(labels))
page=Page()
attr=df["pidtime"].tolist()
cpu=df["CPU%"].tolist()
menmory=df["Menmory%"].tolist()
menmorySize=df["Menmory"].tolist()
bar = Line()
bar.set_global_opts(
   title_opts=TitleOpts(title="自助打印折线图",
                        subtitle="CPU/Menmory百分比")
)
t=Timeline()
bar.add_xaxis(attr)
bar.add_yaxis("CPU%",cpu,color="blue",is_smooth=True)
bar.add_yaxis("Menmory%",menmory,color="red")

line=Line()
line.set_global_opts(
    title_opts=TitleOpts(title="自助打印折线图",
                        subtitle="Menmory使用大小（M）")
)
line.add_xaxis(attr)
line.add_yaxis("Menmory",menmorySize,color="blue")
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
t.add(bar,"百分比")
t.add(line,"使用大小")
Page.add(line)
Page.add(bar)
page.render()
# t.render()
