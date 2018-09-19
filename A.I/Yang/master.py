import requests
import json   
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import math
import os
def ascii2(integer_value_entered):

    global valuemover
    global returned_value

    valuemover = integer_value_entered
    if valuemover == 1: 
        returned_value = ""
    elif valuemover == 2:
        returned_value = "a"
    elif valuemover == 3:
        returned_value = "b"
    elif valuemover == 4:
        returned_value = "c"
    elif valuemover == 5:
        returned_value = "d"   
    elif valuemover == 6:
        returned_value = "e"
    elif valuemover == 7:
        returned_value = "f" 
    elif valuemover == 8:
        returned_value = "g"
    elif valuemover == 9:
        returned_value = "h"
    elif valuemover == 10:
        returned_value = "i"
    elif valuemover == 11:
        returned_value = "j"
    elif valuemover == 12:
        returned_value = "k"
    elif valuemover == 13:
        returned_value = "l"
    elif valuemover == 14:
        returned_value = "m"
    elif valuemover == 15:
        returned_value = "n"
    elif valuemover == 16:
        returned_value = "o"
    elif valuemover == 17:
        returned_value = "p"
    elif valuemover == 18:
        returned_value = "q"
    elif valuemover == 19:
        returned_value = "r"
    elif valuemover == 20:
        returned_value = "s"
    elif valuemover == 21:
        returned_value = "t"
    elif valuemover == 22:
        returned_value = "u"
    elif valuemover == 23:
        returned_value = "v"
    elif valuemover == 24:
        returned_value = "w"
    elif valuemover == 25:
        returned_value = "x"
    elif valuemover == 26:
        returned_value = "y"
    elif valuemover == 27:
        returned_value = "z"
    return(returned_value)
def doeswordexist(word):
    firstletter = word[0]
    if ((str((BeautifulSoup(((requests.get('https://en.oxforddictionaries.com/definition/' + word)).text), 'html.parser')).find_all('h3'))).find('[<h3 class="ps pos">') > -1) and ((str((BeautifulSoup(((requests.get('https://en.oxforddictionaries.com/definition/' + word)).text), 'html.parser')).find_all('h3'))).find('<span class="pos">abbreviation') == -1):
        with open(firstletter + '-file.txt', 'r+') as f:
            old = f.read()
            f.seek(0)
            f.write(word + '\n' + old)
            print(word)
def crack():
    os.chdir('..')
    os.chdir('A.I.Words')
    y = 1
    x = 1
    z = 1
    for f in range(19683):
        if y == 28: 
            y = 1
        if x == 730:
            x = 1
        if z == 19684:
            z = 1
        
        place3floored = (math.floor(z / 729) + 1)
        place4floored = (math.floor(x / 27) + 1)
        place5floored = (math.floor(y / 1) + 1)
        place1 = 'a'
        place3 = ascii2(place3floored)
        place4 = ascii2(place4floored)
        place5 = ascii2(place5floored)
        completedword = place1 + place2 + place3 + place4 + place5
        x = x + 1
        y = y + 1
        z = z + 1
        doeswordexist(completedword)
crack()