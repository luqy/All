
# -*- coding: utf-8 -*-
# @Time    : 2020/6/17 14:10
# @Author  : luqy
# @Email   : 
# @File    : ClassDef.py
# @Software: PyCharm
class Father():
    def __init__(self,Html=None,Img=None,name=None,Doc=None,):
        self.Doc = Doc
        self.Html = Html
        self.Img= Img
        self.name=name
        print("doc",self.Doc,type(self.Doc))
        print("Html", self.Html, type(self.Html))
        print("Img", self.Img, type(self.Img))
        print("name",self.name,type(self.name))
    def csname(self):
        print('doc',self.Doc)
        print(type(self.Doc))
    def cs0(self):
        print("你好")
    def cs(self,he0=None,he1=None):
        self.cs0()
        print('name',self.name)
        print(type(self.name))
        rev_to = he0["to_reciver"].split(',')
        rev_cc = he0["cc_reciver"].split(',')
        rev_tt=he0["tt_reciver"].split(",")
        rev=rev_to+rev_cc
        print(rev)
        print('-----')


