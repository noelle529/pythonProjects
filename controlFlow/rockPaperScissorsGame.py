#rock paper scissors app
import random

userInput = input('Enter a choice [rock/paper/scissor]: ')

possibleActions = ['rock', 'paper', 'scissor']
computerAction = random.choice(possibleActions)
print('Computer chooses: ' + str(computerAction))


def game():
    while True:
        if userInput == computerAction:
            print('It is a draw.')
        elif userInput == 'rock':
            if computerAction == 'scissor':
                print('You win!')
            else: 
                print('Paper covers rock. You lose.')
        elif userInput == 'paper':
            if computerAction == 'rock':
                print('You win!')
            else: 
                print('Scissors cuts paper. You lose.')
        elif userInput == 'scissor':
            if computerAction == 'paper':
                print('You win!')
            else: 
                print('Rock smashes scissor. You lose.')

            playAgain = input('Play again? [y/n]: ')
            if playAgain.lower() != 'y':
                break
            else:
                game()