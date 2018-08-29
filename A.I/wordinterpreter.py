inputtedsentence = "what is a test?"
split_up_sentence = inputtedsentence.split()
number_of_words = len(split_up_sentence)
response = ""
finalword = split_up_sentence[(number_of_words - 1)]
length_of_final_word = len(finalword)
final_character = finalword[length_of_final_word - 1]
firstword = split_up_sentence[0]
secondword = split_up_sentence[1]
thirdword = split_up_sentence[2]

if final_character == "?":
    sentence_is_question = True
else:
    sentence_is_question = False

if (firstword == "What" or firstword == "what") and (secondword == "is") and (thirdword == "a" or "an") and (sentence_is_question == True):
    sentenceid = "wikiquestion"
else:
    sentenceid = "False"

print(sentenceid)