
import platform
import random
import os

class Tutorial:
    def __init__(self):
        a=1

    #Helper function to generate random numbers for the tutorials.
    def randomValues(self, a, b, c, d):
        while(True):
            term1 = random.randint(a, b)
            term2 = random.randint(c, d)
            if((term1 - term2) >= 0): break
        return (term1,term2)


    #Primary method for running/managing the Practice tutorial.
    def startPracticeTutorial(self, mode):
        displayFunction('clear', '')

        #The Addition Practice Tutorial.
        if(mode == 'addition'):
            counter = 0
            while(counter < 5):

                #Generate the random values for the problem.
                terms = self.randomValues(0, 20, 0, 20)
                answer = terms[0] + terms[1]

                #Prompt the User with the random problem.
                displayFunction('normal', "\n\n\n\nCan you solve this problem?")
                displayFunction('normal', str(terms[0]) + ' + ' + str(terms[1]) + ' = ???')
                inputNumber = inputFunction('number', 'Enter your answer (or enter  -1  for a hint):  ')

                #Process a request for a hint.
                if(inputNumber == -1):
                    hintTerms = self.randomValues(0, 20, 0, 20)
                    hintAnswer = hintTerms[0] + hintTerms[1]
                    displayFunction('normal', '\n\n\nHere\'s another similar problem: ' + str(hintTerms[0]) + ' + ' + str(hintTerms[1]) + ' = ' + str(hintAnswer) + '.')
                    displayFunction('normal', 'If it helps, try counting out the numbers using your fingers (and don\'t forget, you have toes, too!)')
                    continue

                #Process the correct answer..
                if(inputNumber == answer):
                    displayFunction('normal', "\nThe correct answer is: " + str(answer) + ".")
                    displayFunction('normal', "You're right! Great Job!!")

                #Process the INCORRECT answer.
                else:
                    displayFunction('normal', "Almost, the correct answer is: " + str(answer) + ".")
                    displayFunction('normal', "But keep trying, you're doing good!")

                counter += 1
                if(counter >= 5):
                    displayFunction('normal', "\n\n\n\nThat's five practice attempts! \nGood job, now go back to the previous menu and choose another lesson.")
                    inputFunction('char', 'Press the Enter key to continue...')

        #The Subtraction Practice Tutorial.
        if(mode == 'subtraction'):
            counter = 0
            while(counter < 5):
                #Generate the random values for the problem.
                terms = self.randomValues(0, 20, 0, 20)
                answer = terms[0] - terms[1]

                #Prompt the User with the random problem.
                displayFunction('normal', "\n\n\n\nCan you solve this problem?")
                displayFunction('normal', str(terms[0]) + ' - ' + str(terms[1]) + ' = ???')
                inputNumber = inputFunction('number', 'Enter your answer (or enter  -1  for a hint):  ')

                #Process a request for a hint.
                if(inputNumber == -1):
                    hintTerms = self.randomValues(0, 20, 0, 20)
                    hintAnswer = hintTerms[0] - hintTerms[1]
                    displayFunction('normal', '\n\n\nHere\'s another similar problem: ' + str(hintTerms[0]) + ' - ' + str(hintTerms[1]) + ' = ' + str(hintAnswer) + '.')
                    displayFunction('normal', 'If it helps, try counting out the numbers using your fingers.')
                    continue

                #Process the correct answer..
                if(inputNumber == answer):
                    displayFunction('normal', "\nThe correct answer is: " + str(answer) + ".")
                    displayFunction('normal', "You're right! Great Job!!")

                #Process the INCORRECT answer.
                else:
                    displayFunction('normal', "Almost, the correct answer is: " + str(answer) + ".")
                    displayFunction('normal', "But keep trying, you're doing good!")

                counter += 1
                if(counter >= 5):
                    displayFunction('normal', "\n\n\n\nThat's five practice attempts! \nGood job, now go back to the previous menu and choose another lesson.")
                    inputFunction('char', 'Press the Enter key to continue...')


        #The Multiplication Practice Tutorial.
        if(mode == 'multiplication'):
            counter = 0
            while(counter < 5):
                #Generate the random values for the problem.
                terms = self.randomValues(0, 10, 0, 10)
                answer = terms[0] * terms[1]

                #Prompt the User with the random problem.
                displayFunction('normal', "\n\n\n\nCan you solve this problem?")
                displayFunction('normal', str(terms[0]) + ' X ' + str(terms[1]) + ' = ???')
                inputNumber = inputFunction('number', 'Enter your answer (or enter  -1  for a hint):  ')

                #Process a request for a hint.
                if(inputNumber == -1):
                    hintTerms = self.randomValues(0, 10, 0, 10)
                    hintAnswer = hintTerms[0] * hintTerms[1]
                    displayFunction('normal', '\n\n\nHere\'s another similar problem: ' + str(hintTerms[0]) + ' X ' + str(hintTerms[1]) + ' = ' + str(hintAnswer) + '.')
                    displayFunction('normal', 'If it helps, try counting out the numbers using your fingers.')
                    continue

                #Process the correct answer..
                if(inputNumber == answer):
                    displayFunction('normal', "\nThe correct answer is: " + str(answer) + ".")
                    displayFunction('normal', "You're right! Great Job!!")

                #Process the INCORRECT answer.
                else:
                    displayFunction('normal', "Almost, the correct answer is: " + str(answer) + ".")
                    displayFunction('normal', "But keep trying, you're doing good!")

                counter += 1
                if(counter >= 5):
                    displayFunction('normal', "\n\n\n\nThat's five practice attempts! \nGood job, now go back to the previous menu and choose another lesson.")
                    inputFunction('char', 'Press the Enter key to continue...')


        #The Division Practice Tutorial.
        if(mode == 'division'):
            counter = 0
            while(counter < 5):
                #Generate the random values for the problem.
                terms = self.randomValues(1, 27, 1, 9)
                answer = terms[0] // terms[1]
                remainder = terms[0] % terms[1]

                #Prompt the User with the random problem.
                displayFunction('normal', "\n\n\n\nCan you solve this problem?")
                displayFunction('normal', str(terms[0]) + ' / ' + str(terms[1]) + ' = ???')
                inputNumber = inputFunction('number', 'Enter how many times  ' + str(terms[1]) + '  goes into  ' + str(terms[0]) + '  (or enter  -1  for a hint):  ')
                inputRemainder = inputFunction('number', 'Now enter the remainder: ')

                #Process a request for a hint.
                if(inputNumber == -1):
                    hintTerms = self.randomValues(1, 27, 1, 9)
                    hintAnswer = hintTerms[0] // hintTerms[1]
                    hintRemainder = hintTerms[0] % hintTerms[1]

                    displayFunction('normal', '\n\n\nHere\'s another similar problem: ' + str(hintTerms[0]) + '/' + str(hintTerms[1]) + ' = ' + str(hintAnswer) + '.')
                    displayFunction('normal', 'With a remainder of,  ' + str(hintRemainder) + '.')
                    displayFunction('normal', 'If it helps, try counting out the numbers using your fingers.')
                    continue

                #Process the correct answer..
                if((inputNumber == answer) & (inputRemainder == remainder)):
                    displayFunction('normal', "\nThe correct answer is: " + str(answer) + ', with a remainder of ' + str(remainder) + ".")
                    displayFunction('normal', "You're right! Great Job!!")

                #Process the INCORRECT answer.
                else:
                    displayFunction('normal', "\nAlmost, he correct answer is: " + str(answer) + ', with a remainder of ' + str(remainder) + ".")
                    displayFunction('normal', "But keep trying, you're doing good!")

                counter += 1
                if(counter >= 5):
                    displayFunction('normal', "\n\n\n\nThat's five practice attempts! \nGood job, now go back to the previous menu and choose another lesson.")
                    inputFunction('char', 'Press the Enter key to continue...')




#Primary method for running/managing the Instructional tutorial.
    def startInstructionalTutorial(self, mode):
        displayFunction('clear', '')

        #The Addition Practice Tutorial.
        if(mode == 'addition'):

            #Prompt the User with the random problem.
            displayFunction('normal', "Doing addition is the easiest kind of math there is.")
            displayFunction('normal', "Adding two numbers is really just like counting.")
            displayFunction('normal', "Like this:")
            displayFunction('normal', "2 + 2")
            displayFunction('normal', "First count to 2 on your fingers. Then, count 2 more on your fingers.")
            displayFunction('normal', "Now, how many fingers have you counted?")
            inputFunction('char', '\nThink about it for a moment, then press the Enter key when you\'re ready...')
            displayFunction('normal', "\nif you counted up to 4, then that\'s the right answer!")
            inputFunction('char', '\nPress the Enter key to continue...')
            displayFunction('clear', '')
            displayFunction('normal', "\nNow let's try a different one. Try this problem:")
            hintTerms = self.randomValues(1, 5, 1, 5)
            hintAnswer = hintTerms[0] + hintTerms[1]
            displayFunction('normal', str(hintTerms[0]) + ' + ' + str(hintTerms[1]) + ' = ' + '???')
            displayFunction('normal', '\nRemember, count the first number on the left with your fingers (this time it\'s ' + str(hintTerms[0]) + ' ).')
            displayFunction('normal', 'And now also count the other number, ' + str(hintTerms[1]) + ', with your fingers, too.')
            displayFunction('normal', 'If everything went right, then the total number of fingers you counted should be: ' + str(hintAnswer) + '.')
            inputFunction('char', '\nGood job! Now press the Enter key to continue to go back and pick another lesson...')


        #The Subtraction Practice Tutorial.
        if(mode == 'subtraction'):
            displayFunction('normal', "Doing subtraction is like addition, except now you're taking away and not adding.")
            displayFunction('normal', "And like addition, you can use your fingers to do the counting.")
            displayFunction('normal', "Like this:")
            displayFunction('normal', "4 - 2")
            displayFunction('normal', "First count to 4 on your fingers. Then, take away two fingers.")
            displayFunction('normal', "Now, how many fingers do you have left?")
            inputFunction('char', '\nThink about it for a moment, then press the Enter key when you\'re ready...')
            displayFunction('normal', "\nif you counted down to 2, then that\'s the right answer!")
            inputFunction('char', '\nPress the Enter key to continue...')
            displayFunction('clear', '')
            displayFunction('normal', "\nNow let's try a different one. Try this problem:")
            hintTerms = self.randomValues(1, 10, 1, 8)
            hintAnswer = hintTerms[0] - hintTerms[1]
            displayFunction('normal', str(hintTerms[0]) + ' - ' + str(hintTerms[1]) + ' = ' + '???')
            displayFunction('normal', '\nRemember, count the first number on the left with your fingers (this time it\'s ' + str(hintTerms[0]) + ' ).')
            displayFunction('normal', 'And now take away the second number, ' + str(hintTerms[1]) + ', from what you just counted.')
            displayFunction('normal', 'If everything went right, then the total number of fingers you still have left should be: ' + str(hintAnswer) + '.')
            inputFunction('char', '\nGood job! Now, press the Enter key to continue to go back and pick another lesson...')


        #The Multiplication Practice Tutorial.
        if(mode == 'multiplication'):
            displayFunction('normal', "Doing multiplication is a lot like addition.")
            displayFunction('normal', "The trick is to also use your fingers to do the counting.")
            displayFunction('normal', "Like this:")
            displayFunction('normal', "2 X 2")
            displayFunction('normal', "First count to 2 on your fingers. Then count 2 again on your fingers, for a total of two times.")
            displayFunction('normal', "Now, how many fingers have you counted?")
            inputFunction('char', '\nThink about it for a moment, then press the Enter key when you\'re ready...')
            displayFunction('normal', "\nif you counted up to 4 altogether, then that\'s the right answer!")
            inputFunction('char', '\nPress the Enter key to continue...')
            displayFunction('clear', '')
            displayFunction('normal', "\nNow let's try a different one. Try this problem:")
            hintTerms = self.randomValues(1, 3, 2, 3)
            hintAnswer = hintTerms[0] * hintTerms[1]
            displayFunction('normal', str(hintTerms[0]) + ' X ' + str(hintTerms[1]) + ' = ' + '???')
            displayFunction('normal', '\nRemember, count the first number on the left with your fingers (this time it\'s ' + str(hintTerms[0]) + ' ).')
            displayFunction('normal', 'And now, count ' + str(hintTerms[0]) + ' again, to a total of ' + str(hintTerms[1]) + ' times.')
            displayFunction('normal', 'If everything went right, then the total number of fingers you just counted should be: ' + str(hintAnswer) + '.')
            inputFunction('char', '\nGood job! Now press the Enter key to continue to go back and pick another lesson...')


        #The Division Practice Tutorial.
        if(mode == 'division'):
            displayFunction('normal', "Doing division may seem tough at first, but it's not that bad once you get used to it.")
            displayFunction('normal', "And just like addition, subtraction, and multiplication, you can use your fingers to do the counting.")
            displayFunction('normal', "Like this:")
            displayFunction('normal', "6 / 5")
            displayFunction('normal', "First count to 6 on one hand. Then, count to 5 on the other hand.")
            displayFunction('normal', "Now how many times will 5 go into 6 without going over?")
            displayFunction('normal', "And how many more fingers did you count on the hand with 6, than the hand with 5?")
            inputFunction('char', '\nThink about it for a moment, then press the Enter key when you\'re ready...')
            displayFunction('normal', "\nif you found that five will go into 6 only once, and that there's one finger left over, then that\'s the right answer!")
            inputFunction('char', '\nPress the Enter key to continue...')
            displayFunction('clear', '')
            displayFunction('normal', "\nNow, let's try a different one. Try this problem:")
            hintTerms = self.randomValues(1, 6, 1, 4)
            hintAnswer = hintTerms[0] // hintTerms[1]
            hintRemainder = hintTerms[0] % hintTerms[1]
            displayFunction('normal', str(hintTerms[0]) + ' / ' + str(hintTerms[1]) + ' = ' + '???')
            displayFunction('normal', '\nRemember, first count the number on the left with your fingers (this time it\'s ' + str(hintTerms[0]) + ' ).')
            displayFunction('normal', 'And now count ' + str(hintTerms[1]) + ' on your other hand.')
            displayFunction('normal', 'If everything went right, then ' + str(hintTerms[1]) + ' should go into ' + str(hintTerms[0]) + ',  ' + str(hintAnswer) + ' times.')
            displayFunction('normal', 'And there should be a remainder of ' + str(hintRemainder) + ' fingers on your other hand.')
            inputFunction('char', '\nGood job! Now press the Enter key to continue to go back and pick another lesson...')










#Wrapper function for display text & messages. Note: this is a single location for replacing output
#to the console, with display output driven by PyQT, etc.
def displayFunction(outputMode, outputString):
    if (outputMode == 'normal'):
        print(outputString)
        return None

    if(outputMode == 'clear'):
        print('\n'*10)
        Return: None

#Wrapper function for input text & messages. Note: this is a single location for replacing input
#from the keyboard, with display output driven by PyQT, etc.
def inputFunction(inputMode, inputString):
    if (inputMode == 'number'):
        number = int(input(inputString), 10)    #Get a number from the console in base 10.
        return number

    elif (inputMode == 'char'):
        return(input(inputString))

    else:
        return None

#MAIN():  Entry point for code execution of the Scales application.
def main():

    tutorialObject = Tutorial()

    while(True):

        #Main UI Loop for selecting Practice Tutorial, Instructional Tutorial, or Quitting application.
        displayFunction('normal', 'Please select a Tutorial:')
        displayFunction('normal', '(A)      Arithmetic Practice Tutorial.')
        displayFunction('normal', '(B)      Arithmetic Practice Tutorial.')
        displayFunction('normal', '(Q)      Quit the program')
        input = inputFunction('char', '\nPlease enter your choice: ')

        #PRACTICE TUTORIAL:  Main UI Loop for selecting what type of Practice Tutorial the User wants.
        if((input == 'A') | (input == 'a')):
            while(True):
                displayFunction('clear', '')
                displayFunction('normal', 'Please select if you wan to practice Adding, Subtracting, Multiplication, or Division:')
                displayFunction('normal', '(1)      Practice Addition.')
                displayFunction('normal', '(2)      Practice Subtraction.')
                displayFunction('normal', '(3)      Practice Multiplication.')
                displayFunction('normal', '(4)      Practice Division.')
                displayFunction('normal', '(Q)      Quit to Main Menu.')
                input = inputFunction('char', '\nPlease enter your choice: ')

                #Practice Adding Object initialization and running.
                if(input == '1'):
                    #Call StartTutorial in the PracticeTurial Object.
                    tutorialObject.startPracticeTutorial('addition')

                elif(input == '2'):
                    #Call StartTutorial in the PracticeTurial Object.
                    tutorialObject.startPracticeTutorial('subtraction')

                elif(input == '3'):
                    #Call StartTutorial in the PracticeTurial Object.
                    tutorialObject.startPracticeTutorial('multiplication')

                elif(input == '4'):
                    #Call StartTutorial in the PracticeTurial Object.
                    tutorialObject.startPracticeTutorial('division')

                displayFunction('clear', '')
                if ((input == 'Q') | (input == 'q')):
                    input = 'Z'
                    break


        #INSTRUCTIONAL TUTORIAL:  Main UI Loop for selecting what type of Instructional Tutorial the User wants.
        if((input == 'B') | (input == 'b')):
            while(True):
                displayFunction('clear', '')
                displayFunction('normal', 'Please select if you wan to learn about Adding, Subtracting, Multiplication, or Division:')
                displayFunction('normal', '(1)      Addition Instructional Tutorial.')
                displayFunction('normal', '(2)      Subtraction Instructional Tutorial.')
                displayFunction('normal', '(3)      Multiplication Instructional Tutorial.')
                displayFunction('normal', '(4)      Division Instructional Tutorial.')
                displayFunction('normal', '(Q)      Quit to Main Menu.')
                input = inputFunction('char', '\nPlease enter your choice: ')

                #Practice Adding Object initialization and running.
                if(input == '1'):
                    #Call StartTutorial in the PracticeTurial Object.
                    tutorialObject.startInstructionalTutorial('addition')

                elif(input == '2'):
                    #Call StartTutorial in the PracticeTurial Object.
                    tutorialObject.startInstructionalTutorial('subtraction')

                elif(input == '3'):
                    #Call StartTutorial in the PracticeTurial Object.
                    tutorialObject.startInstructionalTutorial('multiplication')

                elif(input == '4'):
                    #Call StartTutorial in the PracticeTurial Object.
                    tutorialObject.startInstructionalTutorial('division')

                displayFunction('clear', '')
                if ((input == 'Q') | (input == 'q')):
                    input = 'Z'
                    break



        displayFunction('clear', '')
        if ((input == 'Q') | (input == 'q')): break

if __name__ == '__main__': main()
