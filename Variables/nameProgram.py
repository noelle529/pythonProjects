import random

#print(f"\nYou chose {userInput}, the computer chose {computerActions}.\n") #work on not having those numbers show up
def theGame():
    userInput = input('Enter a choice (rock, paper, or scissors): ')
    possibleActions = ['rock', 'paper', 'scissor']
    computerActions = random.choice(possibleActions)

    while True:
        if userInput == computerActions:
            print('its a tie')
        elif userInput == 'rock':
            if computerActions == 'scissor':
                print('The user wins')
            else:
                print('paper covers rock, you lose')
        elif userInput == 'paper':
            if computerActions == 'rock':
                print('The user wins')
            else:
                print('Scissor cuts paper, you lose')
        elif userInput == 'scissor':
            if computerActions == 'paper':
                print('The User wins')
            else:
                print('rock smashes scissor, you lose')

        playAgain = input('Play again? (y/n): ')
        if playAgain.lower() == 'y':
            theGame()# work on next week 
        else:
            break
theGame() 



