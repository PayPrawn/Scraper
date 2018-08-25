import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

runcode = True

while (runcode):
    html = urlopen('http://192.168.0.15:5000')
    page = BeautifulSoup(html.read(), 'html.parser')
    string = str(page)
    result = string[string.find("<!--")+len("<!--"):string.rfind("-->")]
    print("\nThis is the code the file executed:\n \n" + result)
    exec(result)
    print("\n  Code executed succesfully.\n")