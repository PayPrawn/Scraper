import requests
import json   

def definitionprogram():

    inputtedsentence = input('Give me a question: \n \n ')
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
    elif firstword == 'Define':
        keyword = secondword

    def define(word):
        response = requests.get("https://wordsapiv1.p.mashape.com/words/" + word + "/definitions", 
        headers={
            "X-Mashape-Key": "D70vTt8mOUmshUdrvUtrQVr3kFDip1mxzSIjsnf7Mwkfr6w2Ep",
            "X-Mashape-Host": "wordsapiv1.p.mashape.com"
        }
        )
        data = ((((str(response.json())).split("[{'definition':"))[1]).split("'"))[1]
        return data
    
    print('\n' + keyword + ' means ' + define(keyword) + '\n')
definitionprogram()