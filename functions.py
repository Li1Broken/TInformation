from prototipe import *
import re

#decoder

def decode(input):
    currentPM = [None] * 4
    nextPM = [None] * 4
    path = [[0 for x in xrange(len(input) / 2)] for y in xrange(4)]
    currentPM[0] = 0
    currentPM[1] = float("inf")
    currentPM[2] = float("inf")
    currentPM[3] = float("inf")

    i = 0
    while (i < len(input)):
        str = input[i: i + 2]
        if (str == '00'):
            if (currentPM[0] < currentPM[1] + 1):
                nextPM[0] = currentPM[0]
                path[0][i / 2] = 0
            else:
                nextPM[0] = currentPM[1] + 1
                path[0][i / 2] = 1

            if (currentPM[2] + 2 < currentPM[3] + 1):
                nextPM[1] = currentPM[2] + 2
                path[1][i / 2] = 2
            else:
                nextPM[1] = currentPM[3] + 1
                path[1][i / 2] = 3

            if (currentPM[0] + 2 < currentPM[1] + 1):
                nextPM[2] = currentPM[0] + 2
                path[2][i / 2] = 0
            else:
                nextPM[2] = currentPM[1] + 1
                path[2][i / 2] = 1

            if (currentPM[2] < currentPM[3] + 1):
                nextPM[3] = currentPM[2]
                path[3][i / 2] = 2
            else:
                nextPM[3] = currentPM[3] + 1
                path[3][i / 2] = 3


        elif (str == '01'):
            if (currentPM[0] + 1 < currentPM[1] + 2):
                nextPM[0] = currentPM[0] + 1
                path[0][i / 2] = 0
            else:
                nextPM[0] = currentPM[1] + 2
                path[0][i / 2] = 1

            if (currentPM[2] + 1 < currentPM[3]):
                nextPM[1] = currentPM[2] + 1
                path[1][i / 2] = 2
            else:
                nextPM[1] = currentPM[3]
                path[1][i / 2] = 3

            if (currentPM[0] + 1 < currentPM[1]):
                nextPM[2] = currentPM[0] + 1
                path[2][i / 2] = 0
            else:
                nextPM[2] = currentPM[1]
                path[2][i / 2] = 1

            if (currentPM[2] + 1 < currentPM[3] + 2):
                nextPM[3] = currentPM[2] + 1
                path[3][i / 2] = 2
            else:
                nextPM[3] = currentPM[3] + 2
                path[3][i / 2] = 3
        ###############################

        elif (str == '10'):
            if (currentPM[0] + 1 < currentPM[1]):
                nextPM[0] = currentPM[0] + 1
                path[0][i / 2] = 0
            else:
                nextPM[0] = currentPM[1]
                path[0][i / 2] = 1

            if (currentPM[2] + 1 < currentPM[3] + 2):
                nextPM[1] = currentPM[2] + 1
                path[1][i / 2] = 2
            else:
                nextPM[1] = currentPM[3] + 2
                path[1][i / 2] = 3

            if (currentPM[0] + 1 < currentPM[1] + 2):
                nextPM[2] = currentPM[0] + 1
                path[2][i / 2] = 0
            else:
                nextPM[2] = currentPM[1] + 2
                path[2][i / 2] = 1

            if (currentPM[2] + 1 < currentPM[3]):
                nextPM[3] = currentPM[2] + 1
                path[3][i / 2] = 2
            else:
                nextPM[3] = currentPM[3]
                path[3][i / 2] = 3
        #########################################
        elif (str == "11"):
            if (currentPM[0] + 2 < currentPM[1] + 1):
                nextPM[0] = currentPM[0] + 2
                path[0][i / 2] = 0
            else:
                nextPM[0] = currentPM[1] + 1
                path[0][i / 2] = 1

            if (currentPM[2] < currentPM[3] + 1):
                nextPM[1] = currentPM[2]
                path[1][i / 2] = 2
            else:
                nextPM[1] = currentPM[3] + 1
                path[1][i / 2] = 3

            if (currentPM[0] < currentPM[1] + 1):
                nextPM[2] = currentPM[0]
                path[2][i / 2] = 0
            else:
                nextPM[2] = currentPM[1] + 1
                path[2][i / 2] = 1

            if (currentPM[2] + 2 < currentPM[3] + 1):
                nextPM[3] = currentPM[2] + 2
                path[3][i / 2] = 2
            else:
                nextPM[3] = currentPM[3] + 1
                path[3][i / 2] = 3

        i = i + 2
        currentPM = nextPM[:]

    index = currentPM.index(min(currentPM))
    return (constructPath(path, index))

