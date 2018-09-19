import os
os.chdir('A.I.Words')
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
for i in range(2, 28):
    os.system('del ' + ascii2(i) + '-file.txt')
    os.system('NUL> ' + ascii2(i) + '-file.txt')