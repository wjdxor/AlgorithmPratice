import requests 
import json 
# GET 
res = requests.get('http://apis.data.go.kr/3120000/bizUtil/data?serviceKey=OfJRD4FTDToxwYcjmf7xMNJ6v07sE3IhZxn2xGB0t1tLMrHv%2FP8mbPcCln409zA3kTQB7KZ84TsbStxaa%2B6KuA%3D%3D&numOfRows=10&pageNo=1&date=20210101&time=1')
print(str(res.status_code) + " | " + res.text) 
# POST (JSON) 
headers = {'Content-Type': 'application/json; chearset=utf-8'} 
data = {'title': 'dummy title', 'id': 1, 'message': 'hello world!'} 
res = requests.post('http://127.0.0.1:5000', 
data=json.dumps(data), headers=headers) 
print(str(res.status_code) + " | " + res.text)