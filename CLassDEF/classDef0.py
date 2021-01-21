from CLassDEF.ClassDef import Father
class classdef3(Father):
    def __init__(self,Html=None,Img=None,DOC=None):
        super(classdef3,self).__init__(Html=None,Img=None)
        self.DOC=DOC
        print(self.DOC, self.Html, self.Doc, self.Img, self.name)
    def cls2(self):
        self.csname()
        print(self.Doc)
if __name__ == '__main__':
    a=classdef3
    a.cls2()
    a.csname()
