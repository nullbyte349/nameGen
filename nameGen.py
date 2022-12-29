import requests
import sys
import time
from random import randint

def string_replacement(word, word2 = None):
    if settings['singleWord'] == True:
        temp = str(word).replace('b', '')
        temp = str(temp).replace("'", '')
        temp = str(temp).replace('[', '')
        temp = str(temp).replace('"', '')
        temp = str(temp).replace(']', '')
        if settings['NumbersGen'] == True:
            return str(temp) + str(randint(0, 1000))
        elif settings['NumbersGen'] == False:
            return temp

    elif settings['twoWordsJoined'] == True:

        temp = str(word).replace('b', '')
        temp = str(temp).replace("'", '')
        temp = str(temp).replace('[', '')
        temp = str(temp).replace('"', '')
        temp = str(temp).replace(']', '')

        temp2 = str(word2).replace('b', '')
        temp2 = str(temp2).replace("'", '')
        temp2 = str(temp2).replace('[', '')
        temp2 = str(temp2).replace('"', '')
        temp2 = str(temp2).replace(']', '')

        return temp + temp2.capitalize()

def connection():
    if settings['singleWord'] == True:
        clientConnection = requests.get("https://random-word-api.herokuapp.com/word")
        word = clientConnection.content

        print(string_replacement(word))

    elif settings['twoWordsJoined'] == True:
        clientConnection = requests.get("https://random-word-api.herokuapp.com/word")
        time.sleep(0.5) # i'm scared of being rate limited
        clientConnection2 = requests.get("https://random-word-api.herokuapp.com/word")
        word = clientConnection.content
        word2 = clientConnection2.content
        if settings['NumbersGen'] == True:
            word2 = str(word2) + str(randint(0, 1000))
            print(string_replacement(word, word2))
        else:
            print(string_replacement(word, word2))

settings = {
    'singleWord': False,
    'twoWordsJoined': False,
    'NumbersGen': False
}

print("Current settings and their current values:", settings)

print("\nConfiguring: ")
configing, configing2, configing3 = input("Enable? (singleWord: Y/N | twoWordsJoined: Y/N | NumbersGen: Y/N: ").split()

if configing == "Y":
    settings["singleWord"] = True
    if configing3 == "Y":
        settings['NumbersGen'] = True
        connection()
    else:
        connection()

if configing2 == "Y":
    settings["twoWordsJoined"] = True
    if configing3 == "Y":
        settings['NumbersGen'] = True
        connection()
    else:
        connection()

elif configing == "N" and configing2 == "N" and configing3 == "N":
    print("Exiting...")
    time.sleep(3)
    sys.exit()
