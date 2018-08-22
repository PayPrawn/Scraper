import urllib.request
from bs4 import BeautifulSoup
website = 'https://www.supremenewyork.com/shop/all/t-shirts'
selectedpage = urllib.request.urlopen(website)
soup = BeautifulSoup(selectedpage, 'html.parser')
name_box = soup.find('h1', attrs={'a class':'name-link'})
print(name_box)



#div class="header__575b0a15"
#h2