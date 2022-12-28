# HOLY SHIT I CAN MAKE THIS EXTENSIVE AS FUCK

# TO DO:
# make a function for string replacement
# add letter prefrences like capitlizing, lowercase etc

import requests
import sys
import time

def connection():
    if settings['singleWord'] == True:
        clientConnection = requests.get("https://random-word-api.herokuapp.com/word")
        word = clientConnection.content

        temp = str(word).replace('b', '')
        temp = str(temp).replace("'", '')
        temp = str(temp).replace('[', '')
        temp = str(temp).replace('"', '')
        temp = str(temp).replace(']', '')

        print(temp)
    elif settings['twoWordsJoined'] == True:
        clientConnection = requests.get("https://random-word-api.herokuapp.com/word")
        time.sleep(1.5) # i'm scared of being rate limited
        clientConnection2 = requests.get("https://random-word-api.herokuapp.com/word")
        word1 = clientConnection.content
        word2 = clientConnection2.content

        temp1 = str(word1).replace('b', '')
        temp1 = str(temp1).replace("'", '')
        temp1 = str(temp1).replace('[', '')
        temp1 = str(temp1).replace('"', '')
        temp1 = str(temp1).replace(']', '')

        temp2 = str(word2).replace('b', '')
        temp2 = str(temp2).replace("'", '')
        temp2 = str(temp2).replace('[', '')
        temp2 = str(temp2).replace('"', '')
        temp2 = str(temp2).replace(']', '')

        # personal prefrence for now omegalul   
        test = temp1 + temp2.capitalize()
        print(test)

settings = {
    'singleWord': False,
    'twoWordsJoined': False
}

print("Current settings and their current values:", settings)
print("\tnfo:\n----------------------------------------------------------------------------------------------------------------------")
print("Y to enable singleWord mode")
print("YY to enable twoWordsJoined mode")

print("Configuring: ")
configing = input("Enable? (Y/YY): ");

if configing == "Y":
    settings["singleWord"] = True;
    connection()

elif configing == "YY":
    settings["twoWordsJoined"] = True
    connection()

elif configing == "N":
    print("Exiting...")
    sys.exit();

