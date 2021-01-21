from flask import Flask,request
import json
import os
import sys
app=Flask(__name__)
@app.route("/test_1.0",methods=["get"])
def check():
    return_dict={"return_code":'200','return_info':'处理成功',"result":False}
    print(request.args is None)
    if request.args is None:
        return_dict['return_code']='5004'
        return_dict['return_info']='请求参数为空'
        return json.dumps(return_dict,ensure_ascii=False)
    get_data=request.args.to_dict()
    name=get_data.get('name')
    age=get_data.get('age')
    return_dict['result']=tt(name,age)
    return json.dumps(return_dict, ensure_ascii=False)
@app.route("/test_2.0",methods=['post'])
def checkpost():
    return_dict={"return_code":'300',"return_info":"处理post","result":False}
    username=request.values.get("username")
    pwd=request.values.get("pwd")
    print("1",username)
    print("2",type(pwd))
    if pwd==str(123456):
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    return_dict["result"]=tt(username,pwd)
    return json.dumps(return_dict, ensure_ascii=False)

def tt(name,age):
    result_str='%s今年%s岁' %(name,age)
    return result_str
if __name__ == '__main__':
    app.run(port=7777,host='0.0.0.0',debug=True)