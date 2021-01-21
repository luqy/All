import pandas as pd
path=r"C:\Users\LQY\Desktop\cs.xlsx"
df=pd.read_excel(path,sheet_name='Sheet1',header=None)
date=df.head()
print(date)
nrows=df.shape[0]
ncols=df.columns.size
print("=========================================================================")
print('Max Rows:'+str(nrows))
print('Max Columns'+str(ncols))
print(df.columns)
# for icol in range(ncols):
# #     print(str(icol)+':'+df.columns[icol])