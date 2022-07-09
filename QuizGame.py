#Welcome menu:
print ("""Hello and welcome to my generic quiz!
Rules & Tips:
1. The game will ask you 10 trivia questions from different topics.
2. For every right answer you will get 1 point, for every wrong answer you get no points.
3. If you need a hint, type \"Hint\". You will only get half a point if you're right.
4. You can type your answers in upper or lower case, it does not matter.

""")

playing = input ("If you want to play the game, type \"yes\" to continue: \n")
if playing.lower() != "yes":
    print ("See you next time!")
    input('Press ENTER to exit')
    quit()

print ("\nGreat, let's begin!")
score = 0
print ("************************************\n")

#Question 1:
answer = input ("Question number 1:\nWhen did Facebook launch? ")
if answer.lower() == "2004":
    print ("Correct!\n")
    score += 1
elif answer.lower() == "two thousand and four":
    print ("Correct!\n")
    score += 1
elif answer.lower() == "hint":
    print (">Hint: It is a year between 2000 and 2005")
    answer = input ("Your answer: ")
    if answer.lower() == "2004":
        print ("Correct!\n")
        score += 0.5
    elif answer.lower() == "two thousand and four":
        print ("Correct!\n")
        score += 0.5
    else:
        print ("Incorrect!\nThe right answer is: 2004\n")
else: 
    print ("Incorrect!\nThe right answer is: 2004\n")

#Question 2:
answer = input ("Question number 2:\nWhat is the last letter of the Greek alphabet? ")
if answer.lower() == "omega":
    print ("Correct!\n")
    score += 1
elif answer.lower() == "hint":
    print (">Hint: There's an animated movie called: \"Alpha and _____\"")
    answer = input ("Your answer: ")
    if answer.lower() == "omega":
        print ("Correct!\n")
        score += 0.5
    else:
        print ("Incorrect!\nThe right answer is: Omega\n")
else: 
    print ("Incorrect!\nThe right answer is: Omega\n")

#Question 3:
answer = input ("Question number 3:\nCynophobia is a fear of what? ")
if answer.lower() == "dogs":
    print ("Correct!\n")
    score += 1
elif answer.lower() == "hint":
    print (">Hint: These are four legged, house pet mammals")
    answer = input ("Your answer: ")
    if answer.lower() == "dogs":
        print ("Correct!\n")
        score += 0.5
    else:
        print ("Incorrect!\nThe right answer is: Dogs\n")
else: 
    print ("Incorrect!\nThe right answer is: Dogs\n")

#Question 4:
answer = input ("Question number 4:\nWhat is the most consumed manufactured drink in the world? ")
if answer.lower() == "tea":
    print ("Correct!\n")
    score += 1
elif answer.lower() == "hint":
    print (">Hint: The 2 most populated countries are China and India, what do they drink the most?")
    answer = input ("Your answer: ")
    if answer.lower() == "tea":
        print ("Correct!\n")
        score += 0.5
    else:
        print ("Incorrect!\nThe right answer is: Tea\n")
else: 
    print ("Incorrect!\nThe right answer is: Tea\n")

#Question 5:
answer = input ("Question number 5:\nHow many colors are there in the rainbow? ")
if answer.lower() == "7":
    print ("Correct!\n")
    score += 1
elif answer.lower() == "seven":
    print ("Correct!\n")
    score += 1
elif answer.lower() == "hint":
    print (">Hint: No more than 9, no less than 4")
    answer = input ("Your answer: ")
    if answer.lower() == "7":
        print ("Correct!\n")
        score += 0.5
    elif answer.lower() == "seven":
        print ("Correct!\n")
        score += 0.5
    else:
        print ("Incorrect!\nThe right answer is: Seven\n")
else: 
    print ("Incorrect!\nThe right answer is: Seven\n")


#Question 6:
answer = input ("Question number 6:\nHow many hearts does an octopus have? ")
if answer.lower() == "3":
    print ("Correct!\n")
    score += 1
elif answer.lower() == "three":
    print ("Correct!\n")
    score += 1
elif answer.lower() == "hint":
    print (">No hints for this one.")
    answer = input ("Your answer: ")
    if answer.lower() == "3":
        print ("Correct!\n")
        score += 1
    elif answer.lower() == "three":
        print ("Correct!\n")
        score += 1
    else:
        print ("Incorrect!\nThe right answer is: Three\n")
else: 
    print ("Incorrect!\nThe right answer is: Three\n")

#Question 7:
answer = input ("Question number 7:\nWhat is the world's biggest island? ")
if answer.lower() == "greenland":
    print ("Correct!\n")
    score += 1
elif answer.lower() == "hint":
    print (">Hint: This island's terrain is very different from its name...")
    answer = input ("Your answer: ")
    if answer.lower() == "greenland":
        print ("Correct!\n")
        score += 0.5
    else:
        print ("Incorrect!\nThe right answer is: Greenland\n")
else: 
    print ("Incorrect!\nThe right answer is: Greenland\n")

#Question 8:
answer = input ("Question number 8:\nWhat is the world's longest river? ")
if answer.lower() == "amazon":
    print ("Correct!\n")
    score += 1
elif answer.lower() == "hint":
    print (">Hint: It is also the name of one of the greatest companies in the world")
    answer = input ("Your answer: ")
    if answer.lower() == "amazon":
        print ("Correct!\n")
        score += 0.5
    else:
        print ("Incorrect!\nThe right answer is: Amazon\n")
else: 
    print ("Incorrect!\nThe right answer is: Amazon\n")

#Question 9:
answer = input ("Question number 9:\nThree films have won 11 Academy Awards (which is also the record): \nThe Lord of the Rings: The Return of the King, Ben-Hur and...? ")
if answer.lower() == "titanic":
    print ("Correct!\n")
    score += 1
elif answer.lower() == "hint":
    print (">Hint: There was plenty of room on that door.")
    answer = input ("Your answer: ")
    if answer.lower() == "titanic":
        print ("Correct!\n")
        score += 0.5
    else:
        print ("Incorrect!\nThe right answer is: Titanic\n")
else: 
    print ("Incorrect!\nThe right answer is: Titanic\n")

#Question 10:
answer = input ("Question number 10:\nIn Greek mythology, who was the messanger of the gods? ")
if answer.lower() == "hermes":
    print ("Correct!\n")
    score += 1
elif answer.lower() == "hint":
    print (">Hint: He was not the god of beauty, but his sandals were beautiful")
    answer = input ("Your answer: ")
    if answer.lower() == "hermes":
        print ("Correct!\n")
        score += 0.5
    else:
        print ("Incorrect!\nThe right answer is: Hermes\n")
else: 
    print ("Incorrect!\nThe right answer is: Hermes\n")

#Points earned:
print ("The game has ended,")
if score < 5.5:
    print ("You only achieved " + str(score) + " out of 10 points.\nTry again next time!")
elif score >= 5.5 and score < 8:
    print ("You achieved " + str(score) + " out of 10 points.\nNot bad!")
elif score >= 8:
    print ("Wow! You achieved " + str(score) + " out of 10 points! \nYou're awesome!")

input('Press ENTER to exit')
