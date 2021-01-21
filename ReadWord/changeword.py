import win32com
from win32com.client import Dispatch, constants
path='F:\All\ReadWord\cs.docx'
word =win32com.client.Dispatch("word.application")
word.Visible = 0 # 后台运行
word.DisplayAlerts = 0 # 不显示，不警告
doc = word.Documents.Open(path)
word.Selection.Find.Execute('回归情况2', False, False, False, False, False, True, 1, True, '【回归情况】总计12/激活12', 2)
word.add_picture(r'F:\All\ReadWord\h.png')
'''
上面涉及的 11 个参数说明
         (OldStr--搜索的关键字,
         True--区分大小写,
         True--完全匹配的单词，并非单词中的部分（全字匹配）,
         True--使用通配符,
         True--同音,
         True--查找单词的各种形式,
         True--向文档尾部搜索,
         1,
         True--带格式的文本,
         NewStr--替换文本,
         2--替换个数（0表示不替换，1表示只替换匹配到的第一个，2表示全部替换）
'''

#word.Selection.Find.Execute("url",1,'你好',1)
doc.Save()
doc.Close()
word.Quit()

# w = win32com.client.DispatchEx('Word.Application')
# doc = w.Documents.Open(path)
#
# w.Selection.Find.ClearFormatting()
# w.Selection.Find.Replacement.ClearFormatting()
# w.Selection.Find.Execute('url','你好')
# w.Save()
# w.Close()