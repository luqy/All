import pandas as pd
import os
path="F:\All\pyecharts\csv"
csv_list=os.listdir(path)
df_list=[]
name=["pid","pidname","pidtime","cpu%","menmory%","menmorySize"]
for i in range (len(csv_list)):
    df=pd.read_csv(os.path.join(path,csv_list[i]),names=name)
    df_list.append(df)
h=pd.concat(df_list,axis=1)
print(h)
df=pd.DataFrame(data=h)
#df.to_csv("./Text.csv")

