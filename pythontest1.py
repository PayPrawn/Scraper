import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://192.168.0.15:5000')
page = BeautifulSoup(html.read())
print(page)