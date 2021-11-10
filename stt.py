''''''
url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"
api_key = "?"
headers = {"Content-Type" : "application/octet-stream",
          "Transfer-Encoding" : "chunked",
          "Authorization" : "KakaoAK YOURAPIKEY"
          }
''''''

import requests
import json

def stt():
    with open('heykakao.wav', 'rb') as fp:
        data = fp.read()
    
    res = requests.post(url, headers = headers, data = data)
    print(res.text)

stt()