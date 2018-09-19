import requests
import os
from bs4 import BeautifulSoup
secondstructure = []
twoletterword = []
threeletterword = []
os.chdir('NewA.I')
notstop = 'notstop'
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
    if (str((BeautifulSoup(((requests.get('https://en.oxforddictionaries.com/definition/' + word)).text), 'html.parser')).find_all('h3'))).find('[<h3 class="ps pos">') > -1:
        return True
    else:
        return False
'''
firststructure = input('Enter first letter: ')
for i in range(2, 28):
    if doeswordexist(firststructure + ascii2(i)):
        totalword.append(ascii2(i))
        print(ascii2(i))
print(totalword)
requestremove = input('would you like to remove a letter')
if requestremove == 'yes':
    while notstop != 'stop':
        requestremove = input('would you like to remove a letter')
        totalword.remove(requestremove)
        print(totalword)
'''
def testparameters():
    global secondstructure
    global firststructure
    secondstructure = ['m', 's', 'w']
    firststructure = 'a'
testparameters()
for i in range(len(secondstructure)):
    twoletterword.append(firststructure + secondstructure[i])
    print(twoletterword)
os.system('NUL> ' + firststructure + '-file.txt')
for i in range(len(secondstructure)):
    with open(firststructure + '-file.txt', 'r+') as f:
        old = f.read()
        f.seek(0)
        f.write(twoletterword[i] + '\n' + old)
for i in range(len(twoletterword)):
    if ((twoletterword[i])[0] == 'a') or ((twoletterword[i])[0] == 'u') or ((twoletterword[i])[0] == 'i') or ((twoletterword[i])[0] == 'o') or ((twoletterword[i])[0] == 'y'):
        wordtype = 'vowel'
    else: 
        wordtype = 'consonant' 
for i in range(2, 28):
    if wordtype == 'vowel':
        if doeswordexist(ascii2(i) + twoletterword):
            threeletterword.append(ascii2(i) + twoletterword)
            with open(firststructure + '-file.txt', 'r+') as f:
                old = f.read()
                f.seek(0)
                f.write(threeletterword[i] + '\n' + old)
    elif wordtype == 'consonant':
        if doeswordexist(twoletterword + ascii2(i)):
            threeletterword.append(ascii2(i) + twoletterword)
            with open(firststructure + '-file.txt', 'r+') as f:
                old = f.read()
                f.seek(0)
                f.write(threeletterword[i] + '\n' + old)

    