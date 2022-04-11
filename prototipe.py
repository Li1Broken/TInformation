from functions import *

def perform_viterbi_decoding(txt_1):
    return txt_1

def constructPath(path, index):
    code = ""
    length = len(path[0])
    thisState = index
    for i in range(length-1, -1, -1):
        if(thisState == 0):
            code = code + "0"
        elif(thisState == 1):
            code = code + "0"
        elif(thisState == 2):
            code = code + "1"
        else :
            code = code + "1"
        if(i == -1) :
            thisState = 0
        else :
            thisState = path[thisState][i]