# -*- coding: utf-8 -*-
# @Time    : 2020/6/17 14:18
# @Author  : luqy
# @Email   : 
# @File    : ClassDef2.py
# @Software: PyCharm
from CLassDEF.ClassDef import Father
from CLassDEF.classDef0 import classdef3
if __name__ == '__main__':
    Doc="1"
    Img='2'
    Html='3'
    name='4'
    he0={
        "cc_reciver" : "1695751092@qq.com",
        "to_reciver" : "2386410196@qq.com,luqy2020@163.com",
        "tt_reciver":""
    }
    Send = Father(Doc,Img,Html,name)
    Send.cs(he0=he0,he1="456")
    Send.csname()
    a=classdef3(Html,Img)

