import random
import os
from typing import Counter


#global variables
wordToGuess=""
formedWord=""
strikes=0
doneFlag=False
userInput=""

#constants
MESSAGE_LINES=17
MESSAGE_NAMES=[
    "Start",
    "Strike1",
    "Strike2",
    "Strike3",
    "Strike4",
    "Strike5",
    "End"
    ]

#Functions
def get_messages(): #This function return a dictionary of messages 

    with open("./Hangman_Game_Files/user_interface.txt","r", encoding="utf-8") as f:
        textFile = f.readlines()
        
    counter=0

    message0=[]
    message1=[]
    message2=[]
    message3=[]
    message4=[]
    message5=[]
    message6=[]
     
    for i in textFile:
        if counter<17:
            message0.append(i)
        elif counter<34:
            message1.append(i)
        elif counter<51:
            message2.append(i)
        elif counter<68:
            message3.append(i)
        elif counter<85:
            message4.append(i)
        elif counter<102:
            message5.append(i)
        elif counter<119:
            message6.append(i)
        counter=counter+1

    mess0=""
    mess0=mess0.join(message0)
    mess1=""
    mess1=mess1.join(message1)
    mess2=""
    mess2=mess2.join(message2)
    mess3=""
    mess3=mess3.join(message3)
    mess4=""
    mess4=mess4.join(message4)
    mess5=""
    mess5=mess5.join(message5)
    mess6=""
    mess6=mess6.join(message6)
    

    joinMessages={
        "Start":mess0,
        "Strike1":mess1,
        "Strike2":mess2,
        "Strike3":mess3,
        "Strike4":mess4,
        "Strike5":mess5,
        "End":mess6,
        }
    return joinMessages        


def get_word(): #This function returns the word to guess
    #reference global variables
    global formedWord

    with open("./Hangman_Game_Files/words.txt","r",encoding="utf-8") as f:
        listOfWords=f.readlines()
    wordIndex=random.randint(0,len(listOfWords))
    word=listOfWords[wordIndex].replace("\n","")
    formedWord=len(word)*"X"
    
    return word


def addUserInput(letter): #This funtion add the new letter to the formed Word
    #reference global variables
    global wordToGuess
    global formedWord
    #local variable
    Counter=0
    indexes=[]
    
    for letters in wordToGuess:
        if letter==letters:
            indexes.append(Counter) 
        Counter=Counter+1
    
    for numbers in indexes:
        formedWord=formedWord[:numbers]+letter+formedWord[numbers+1:]
        

    

    

#Main
def run():
    #reference global variables
    global wordToGuess
    global doneFlag
    global formedWord
    global strikes
    global userInput

    strikes=0
    messages = get_messages()
    os.system("cls")
    print(messages["Start"])
    wordToGuess=get_word()
    print(formedWord)
    
    while doneFlag==False:
        try:
            userInput=input("Please enter a leter:").lower()
            if len(userInput)==0 or (not userInput.isalpha) or (" " in userInput) or len(userInput)>1 :
                raise ValueError("The input is empty or is not a letter")
            if userInput in wordToGuess:
                addUserInput(userInput)
                os.system("cls")
                print(messages[MESSAGE_NAMES[strikes]])
                print(formedWord)
                if formedWord == wordToGuess:
                    doneFlag=True
                    os.system("cls")
                    print(messages["End"])
                    print(formedWord)
            else:
                strikes=strikes+1
                os.system("cls")
                print(messages[MESSAGE_NAMES[strikes]])
                print(formedWord)
                if strikes==5:
                    doneFlag=True    


        except ValueError as ve:
            print("You entered " + userInput.upper + " and is not a valid input, you lose a try")
            input("Please press enter to continue")
            strikes=strikes+1
            os.system("cls")
            print(messages[MESSAGE_NAMES[strikes]])
            print(formedWord)
            if strikes==5:
                doneFlag=True


if __name__ == "__main__":
    run()