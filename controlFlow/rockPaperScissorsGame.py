#rock paper scissors app

import random

while True:
    userInput = input('Enter a choice [rock/paper/scissor]: ')

    possibleActions = ['rock', 'paper', 'scissor']
    computerAction = random.choice(possibleActions)
    print('Computer chooses: ' + str(computerAction))
    
    if userInput == computerAction:
        print('It is a draw.')

        playAgain = input('Play again? [y/n]: ')
        if playAgain.lower() == 'y':
            continue
        elif playAgain.lower() == 'n':
            break

    elif userInput == 'rock':
        if computerAction == 'scissor':
            print('You win!')

            playAgain = input('Play again? [y/n]: ')
            if playAgain.lower() == 'y':
                continue
            elif playAgain.lower() == 'n':
                break

        else: 
            print('Paper covers rock. You lose.')

            playAgain = input('Play again? [y/n]: ')
            if playAgain.lower() == 'y':
                continue
            elif playAgain.lower() == 'n':
                break
        
    elif userInput == 'paper':
        if computerAction == 'rock':
            print('You win!')            
            
            playAgain = input('Play again? [y/n]: ')
            if playAgain.lower() == 'y':
                continue
            elif playAgain.lower() == 'n':
                break
            
        else: 
            print('Scissors cuts paper. You lose.')
            
            playAgain = input('Play again? [y/n]: ')
            if playAgain.lower() == 'y':
                continue
            elif playAgain.lower() == 'n':
                break

    elif userInput == 'scissor':
        if computerAction == 'paper':
            print('You win!')
                       
            playAgain = input('Play again? [y/n]: ')
            if playAgain.lower() == 'y':
                continue
            elif playAgain.lower() == 'n':
                break

        else: 
            print('Rock smashes scissor. You lose.')
            
            playAgain = input('Play again? [y/n]: ')
            if playAgain.lower() == 'y':
                continue
            elif playAgain.lower() == 'n':
                break