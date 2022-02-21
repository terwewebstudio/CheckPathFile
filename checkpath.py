import os
path = os.getcwd()
filelist = str(os.listdir(path))
import requests

path = os.getcwd()
print(path)
filelist = str(os.listdir(path))
print(filelist)

apiurl = '192.168.1.1'
#data = {"source" : "เด็กชายลุงเริง", "data" : "มากั๊บ"}
data = {"source" : "เด็กชายลุงเริง","data":filelist}
r = requests.post(url=apiurl, data=data)
print(r.text)
print(r.status_code)
