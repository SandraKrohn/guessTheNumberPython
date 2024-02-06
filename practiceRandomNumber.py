import random, sys

def guessTheNumber():
    print('Guess the number between 1 and 100.')
    secretNumber = random.randint(1, 100)
    while True:
        guess = input()
        if guess.isdigit():
            if int(guess) > secretNumber:
                print('Too high, try again!')
            elif int(guess) < secretNumber:
                print('Too low, try again!')
            else:
                print(f'That\'s correct, the secret number was {secretNumber}.')
                print('Play again? y/n')
                keepPlaying = input()
                if not keepPlaying.lower() == 'y' and not keepPlaying.lower() == 'n':
                    print('Please enter y or n.')
                elif keepPlaying.lower() == 'y':
                    print('Guess the number between 1 and 100.')
                    secretNumber = random.randint(1, 100)
                else:
                    print('Bye!')
                    sys.exit()
        else:
            print('Please enter an integer.')

guessTheNumber()