import bs4
from urllib import request
res = request.get('http://nostarch.com')
res.raise_for_status()
nostarchsoup= bs4.beautifulsoup(res.text)
type(nostarchsoup)