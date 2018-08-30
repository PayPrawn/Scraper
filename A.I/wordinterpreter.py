import requests
import json
inputtedsentence = input('Give me a question: \n \n ')
split_up_sentence = inputtedsentence.split()
number_of_words = len(split_up_sentence)
response = ""
finalword = split_up_sentence[(number_of_words - 1)]
length_of_final_word = len(finalword)
final_character = finalword[length_of_final_word - 1]
if number_of_words == 4:
    firstword = split_up_sentence[0]
    secondword = split_up_sentence[1]
    thirdword = split_up_sentence[2]
    fourthword = split_up_sentence[3]
elif number_of_words == 2:
    firstword = split_up_sentence[0]
    secondword = split_up_sentence[1]
elif number_of_words == 6:
    firstword = split_up_sentence[0]
    secondword = split_up_sentence[1]
    thirdword = split_up_sentence[2]
    fourthword = split_up_sentence[3]
    fifthword = split_up_sentence[4]
    sixthword = split_up_sentence[5]

if final_character == "?":
    sentence_is_question = "True"
else:
    sentence_is_question = "False"

if ((firstword == 'What' or firstword == 'what') and (secondword == 'does') and (fourthword == 'mean?' or fourthword == 'mean')) and (number_of_words == 4):
    sentenceid = 'definition'
elif ((firstword == 'define' or firstword == 'Define')) and (number_of_words == 2):
    sentenceid = 'definition2'
elif ((firstword == 'What' or firstword == 'what') and (secondword == 'is') and (thirdword == 'the') and (fourthword == 'definition') and (fifthword == 'of')) and (number_of_words == 6):
    if sixthword.endswith('?'):
        sixthword = sixthword.split('?')
        sixthword = sixthword[0]
    sentenceid = 'definition3'
elif (firstword == 'What' or firstword == 'what') and (secondword == 'is') and (thirdword == 'a' or thirdword == 'an') and (number_of_words == 4):
    sentenceid = 'question'


def define(word):
    response = requests.get("https://wordsapiv1.p.mashape.com/words/" + word + "/definitions", 
    headers={
        "X-Mashape-Key": "D70vTt8mOUmshUdrvUtrQVr3kFDip1mxzSIjsnf7Mwkfr6w2Ep",
        "X-Mashape-Host": "wordsapiv1.p.mashape.com"
    }
    )
    data = str(response.json())
    data = data.split("[{'definition':")
    data = data[1]
    data = data.split("'")
    data = data[1]
    return data

if sentenceid == 'definition':
    print('\n \n' + thirdword + ' means ' + define(thirdword) + '\n \n')
elif sentenceid == 'definition2':
    print('\n \n' + secondword == ' means ' + define(secondword)+ '\n \n')
elif sentenceid == 'definition3':
    print('\n \n' + sixthword + ' means ' + define(sixthword) + '\n \n')

