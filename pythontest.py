import urllib.request
from bs4 import BeautifulSoup
quote_page = 'http://www.supremenewyork.com/shop/all/t-shirts'
page = urllib2.urlopen(quote_page)
page