import pandas as pd
path='F:\All\禅道\eWord.html'
h=pd.read_html(path)[0]
print(h.columns)
print(h.head(4))
