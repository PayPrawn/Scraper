import requests
from bs4 import BeautifulSoup
def doeswordexist(word):
    if (str((BeautifulSoup(((requests.get('https://en.oxforddictionaries.com/definition/' + word)).text), 'html.parser')).find_all('h3'))).find('[<h3 class="ps pos">') > -1:
        return True
    else:
        return False
firststructure = input('Input the first letter of first structure:\n ')
for i in range(26):
    target = (firststructure + ascii(i + 71))
    if doeswordexist(target) == True:
        print()
        
        
        
#ascii 97 - 122