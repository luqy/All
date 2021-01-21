from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line
import pandas as pd
df=pd.read_csv(r"F:\All\pyecharts\csv\TomTaw.eWord.AutomaticTeller.exe_1188.csv")
attr=df["pidtime"].tolist()
cpu=df["CPU%"].tolist()
menmory=df["Menmory%"].tolist()
menmorySize=df["Menmory"].tolist()
line1 = (
    Line()
    .add_xaxis(attr)
    .add_yaxis("CPU占比", cpu)
    .add_yaxis("menmory占比", menmory)
    .set_global_opts(title_opts=opts.TitleOpts(title="内存CPU占比"))
)
line = (
    Line()
    .add_xaxis(attr)
    .add_yaxis("Menmory", menmorySize)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="内存所用大小（M）", pos_top="48%"),
        legend_opts=opts.LegendOpts(pos_top="48%"),
    )
)

grid = (
    Grid()
    .add(line1, grid_opts=opts.GridOpts(pos_bottom="60%"))
    .add(line, grid_opts=opts.GridOpts(pos_top="60%"))
    .render("grid_vertical.html")
)
