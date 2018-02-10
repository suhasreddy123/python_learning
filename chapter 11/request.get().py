import webbrowser
import requests
res=requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
res.ststus_code==requests.codes.ok
len(res.text)
print(res.text[:250])