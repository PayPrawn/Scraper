import requests
import numpy as np
import matplotlib.pyplot as plt
import json   
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import math
start_time = time.time()
realwords = []

def ascii2(integer_value_entered):
    global valuemover
    global returned_value

    valuemover = integer_value_entered
    if valuemover == 1: 
        returned_value = "a"
    elif valuemover == 2:
        returned_value = "b"
    elif valuemover == 3:
        returned_value = "c"
    elif valuemover == 4:
        returned_value = "d"
    elif valuemover == 5:
        returned_value = "e"   
    elif valuemover == 6:
        returned_value = "f"
    elif valuemover == 7:
        returned_value = "g" 
    elif valuemover == 8:
        returned_value = "h"
    elif valuemover == 9:
        returned_value = "i"
    elif valuemover == 10:
        returned_value = "j"
    elif valuemover == 11:
        returned_value = "k"
    elif valuemover == 12:
        returned_value = "l"
    elif valuemover == 13:
        returned_value = "m"
    elif valuemover == 14:
        returned_value = "n"
    elif valuemover == 15:
        returned_value = "o"
    elif valuemover == 16:
        returned_value = "p"
    elif valuemover == 17:
        returned_value = "q"
    elif valuemover == 18:
        returned_value = "r"
    elif valuemover == 19:
        returned_value = "s"
    elif valuemover == 20:
        returned_value = "t"
    elif valuemover == 21:
        returned_value = "u"
    elif valuemover == 22:
        returned_value = "v"
    elif valuemover == 23:
        returned_value = "w"
    elif valuemover == 24:
        returned_value = "x"
    elif valuemover == 25:
        returned_value = "y"
    elif valuemover == 26:
        returned_value = "z"
   

    return(returned_value)

def crack():
    y = 0
    x = 0
    z = 0
    w = 0
    a = 0
    for f in range(26**4):
        if y == 26: 
            y = 0
        if x == 676:
            x = 0
        if z == 17576:
            z = 0
        if w == 456976:
            w = 0
        place1floored = math.floor(y / 1)
        place2floored = (math.floor(x / 26) + 1)
        place3floored = (math.floor(z / 676) + 1)
        place4floored = (math.floor(w / 17576) + 1)
        place5floored = (math.floor(a / 456976) + 1)
        place1 = ascii2(place1floored)
        place2 = ascii2(place2floored)
        place3 = ascii2(place3floored)
        place4 = ascii2(place4floored)
        place5 = ascii2(place5floored)
        completedword = place1 + place2 + place3 + place4 + place5
        x = x + 1
        y = y + 1
        z = z + 1
        w = w + 1
        a = a + 1
        return completedword

def doeswordexist(word):
    if (str((BeautifulSoup(((requests.get('https://en.oxforddictionaries.com/definition/' + word)).text), 'html.parser')).find_all('h3'))).find('[<h3 class="ps pos">') > -1:
        realwords.append(word)
def define(word):
    response = requests.get("https://wordsapiv1.p.mashape.com/words/" + word + "/definitions", 
    headers={
        "X-Mashape-Key": "D70vTt8mOUmshUdrvUtrQVr3kFDip1mxzSIjsnf7Mwkfr6w2Ep",
        "X-Mashape-Host": "wordsapiv1.p.mashape.com"
    }
    )
    data = ((((str(response.json())).split("[{'definition':"))[1]).split("'"))[1]
    return data
def definitionprogram():
    inputtedsentence = input('\n Give me a question: \n \n ')
    split_up_sentence = inputtedsentence.split()
    number_of_words = len(split_up_sentence)
    firstword = split_up_sentence[0]
    secondword = split_up_sentence[1]
    if number_of_words == 4:
        thirdword = split_up_sentence[2]
        fourthword = split_up_sentence[3]
    elif number_of_words == 6:
        thirdword = split_up_sentence[2]
        fourthword = split_up_sentence[3]
        fifthword = split_up_sentence[4]
        sixthword = split_up_sentence[5]
    firstword = firstword.title()

    if ((firstword == 'What') and (secondword == 'does') and (fourthword == 'mean?' or fourthword == 'mean')) and (number_of_words == 4):
        keyword = thirdword
    elif ((firstword == 'What') and (secondword == 'is') and (thirdword == 'the') and (fourthword == 'definition') and (fifthword == 'of')) and (number_of_words == 6):
        if sixthword.endswith('?'):
            sixthword = (sixthword.split('?'))[0]
            keyword = sixthword
        else:
            keyword = sixthword
    elif firstword == 'Define':
        keyword = secondword
    print('\n' + keyword + ' means ' + define(keyword) + '\n')
def wordinterpreter():
    print('\n Command list: \n define')
    x = ''
    while x != 'stop':
        print('\n')
        x = input('input command ')
        if x == 'define':
            definitionprogram()
            while input('Do you want to find out the definition of another word? \n \n') == 'yes':
                definitionprogram()
                print('\n')
def creatematrix():
    x = np.array(10)
    formula = ((((-1 * x) ** 2) + 5) ** (1 / 2))
    y = formula
    plt.plot(x, y)
    plt.show()
    plt.title('Personality Matrix')
def strengthconnection(firstnode, secondnode):
    for i in range(len(connections)):
        if (connections[i][0] == firstnode) and (connections[i][1] == secondnode):
            return connections[i][2]
def nodes():
    global connections
    layer1 = list()
    layer2 = list()
    connections = list()
    for i in range(2):
        layer2.append(["L1-" + str(i)])

    for i in range(10):
        layer1.append(["L2-" + str(i)])
        for n in range(len(layer2)):
            layer1[i].append(layer2[n][0])
            connections.append(["L1-"+ str(i),"L2-"+ str(n),0.5])


    f = open('connections.txt','w')
    a = connections
    f.write(str(a))
    f.close()


    print(layer1)
    print("\n ------------------------------ \n")
    print(layer2)
    print("\n ------------------------------ \n")
    print(connections)
    print("\n ------------------------------ \n")
    print(strengthconnection("L1-9","L2-0"))

print(time.time() - start_time)