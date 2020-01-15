import random

secertNumber = int(random.randrange(10))
triesAttempted = int(1) 

guessNUmber = int(input('Take a guess : '))



while secertNumber != guessNUmber:
    if secertNumber > guessNUmber :
        guessNUmber = int(input('Guess a higher number : '))
        triesAttempted += triesAttempted
    elif secertNumber < guessNUmber : 
        guessNUmber = int(input('Guess a lower number : '))
        triesAttempted += triesAttempted



print ("congrats the number was " + str(secertNumber))
print ("It took you :" + str(triesAttempted) + "attempts")