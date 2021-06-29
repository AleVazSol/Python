import random

def message(correctNumber,guessedNumber):
    if int(guessedNumber)<int(correctNumber):
        return("Incorrect number, please try a higher number:")
    else:
        return("Incorrect number, please try a lower number:")



def run():
    number= random.randint(1,100)
    presentation="""
    GUESS THE NUMBER GAME!!
    Choose a number betwen 1 and 100: 
    """
    userNumber=int(input(presentation))
    while int(userNumber)!= int(number):
        print(message(number,userNumber))
        userNumber=input()
    print("Correct!! the number is "+str(userNumber))


if __name__ == '__main__':
    run()
