#Apache、WSGIでのサンプル
#変更したよ
import sys
import json
import os
from datetime import datetime
#import requests
import shutil
from numpy.random import *
import MySQLdb
import time
import ast
import base64

def application(environ,start_response):
    status = '200 OK'
    body = json.loads(environ['wsgi.input'].read())
    if 'POST'!=environ.get('REQUEST_METHOD'):
        outputstr = {"httperror": {"code": 1}}
        outputjson = json.dumps(outputstr).encode('utf-8')
        response_header = [('Content-type','application/json'),
                        ('Content-Length',str(len(outputjson)))]						
        start_response(status,response_header)
        return [outputjson]
   
    jobcode="xxx"
    if "requestjob" in body.keys():
        requestjob = body["requestjob"]
        jobcode = requestjob["jobcode"]
    else:
        outputstr = {"jsonerror": {"code": 1}}
        outputjson = json.dumps(outputstr).encode('utf-8')
        response_header = [('Content-type','application/json'),
                        ('Content-Length',str(len(outputjson)))]						
        start_response(status,response_header)
        return [outputjson]
    #JSONデータの保存サンプルは例として単純にファイルで保存する例
    f = open("/tmp/"+jobcode+".json", "w")
    json.dump(body, f)
    f.close()
　　　　#重要、ＪＳＯＮを受取確認できたら以下結果を送信する
    outputstr = {"status": "accepted"}
    outputjson = json.dumps(outputstr).encode('utf-8')
    response_header = [('Content-type','application/json'),
                    ('Content-Length',str(len(outputjson)))]						
    start_response(status,response_header)	
    return [outputjson]
