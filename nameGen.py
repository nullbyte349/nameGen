# HOLY SHIT I CAN MAKE THIS EXTENSIVE AS FUCK

# TO DO:
# make a function for string replacement
# add letter prefrences like capitlizing, lowercase etc

import requests
import sys
import time

def string_replacement(word, word2 = None):
    if settings['singleWord'] == True:
        temp = str(word).replace('b', '')
        temp = str(temp).replace("'", '')
        temp = str(temp).replace('[', '')
        temp = str(temp).replace('"', '')
        temp = str(temp).replace(']', '')

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

        print(string_replacement(word, word2))

settings = {
    'singleWord': False,
    'twoWordsJoined': False
}

print("Current settings and their current values:", settings)
print("\ninfo:\n-----------------------------------------------------------------------------------")
print("Y to enable  |  singleWord    | mode")
print("YY to enable | twoWordsJoined | mode\n-----------------------------------------------------------------------------------")

print("\nConfiguring: ")
configing = input("Enable? (Y/YY): ");

if configing == "Y":
    settings["singleWord"] = True;
    connection()

elif configing == "YY":
    settings["twoWordsJoined"] = True
    connection()

else:
    print("Exiting...")
    time.sleep(3)
    sys.exit()
