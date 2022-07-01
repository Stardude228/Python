import random

def hangman():
    if attempts == 5:
        print(
        '''
        +---+
        |   |
            |
            |
            |
            |
        =========
        '''
        )
    elif attempts == 4:
        print(
        '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========
        '''
        )
    elif attempts == 3:
        print(
        '''
       +---+
       |   |
       O   |
       |   |
           |
           |
        =========
        '''
        )
    elif attempts == 2:
        print(
        '''
       +---+
       |   |
       O   |
      /|\  |
           |
           |
        =========
        '''
        )
    elif attempts == 1:
        print(
        '''
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
       =========
        '''
        )
    elif attempts == 0:
        print(
        '''
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
       =========
        '''
        )

choices = ['hammer', 'water', 'milk', 'bread']
desire = 'not chosen'

while desire not in ('YES', 'NO'):
    desire = input('Do you want to play a game? (YES/NO): ').upper()

if desire == 'YES':
    while desire == 'YES':

        random_word = random.choice(choices)
        hidden_word = '*' * len(random_word)
        attempts = 5
        incorrect_letters = []
        print(f'The hidden words is {hidden_word}.')
        print(f'You have {attempts} attempts.')

        while attempts > 0:

            user_inp = input('Type your guess: ').lower()
            hidden_word = list(hidden_word)
            random_word = list(random_word)

            if user_inp in random_word:
                for index, letter in enumerate(random_word):
                    if letter == user_inp:
                        hidden_word[index] = letter
                print(''.join(hidden_word))

                if  hidden_word == random_word:
                    win_word = ''.join(random_word)
                    print(f' You have guessed the hidden word! \n It was {win_word}')
                    desire = input('Do you want to play a game? (YES/NO): ').upper()

                    while desire not in ('YES', 'NO'):
                        desire = input('Do you want to play a game? (YES/NO): ').upper()
                    
                    if desire == 'NO':
                        print('Game over because of the desire!')
                        break

                    elif desire == 'YES':
                        random_word = random.choice(choices)
                        hidden_word = '*' * len(random_word)
                        attempts = 5
                        incorrect_letters = []
                        print(f'The hidden words is {hidden_word}.')
                        print(f'You have {attempts} attempts.')

            else:
                attempts = attempts - 1
                hangman()
                print(f'You have {attempts} attempts left.')
                incorrect_letters.append(user_inp)
                print('The hidden word does not contain such a letter!')
                print(f'The list of letters that are incorrect {incorrect_letters}')

        else:
            desire = input('Do you want to play a game? (YES/NO): ').upper()
            
elif desire == 'NO':
    print('Game over because of the desire!')
