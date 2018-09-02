import requests
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = requests.get('https://en.oxforddictionaries.com/definition/die')
r = BeautifulSoup(url)
data = r.text
string = str(data)
print(string)