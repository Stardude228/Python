import random
number = random.randint(1,10)
choice = 'not defined'
name = input('What is your name? ') 
choice = input('Do you want to play? yes/no ').lower()
number_of_tries = 0
while choice not in ('yes', 'no'):
    choice = input('Please yes or no ').lower()
if choice == 'yes':
    while choice == 'yes':
        try:
            user_num = int(input('Type your guess: '))
            number_of_tries += 1
            if number > user_num:
                print('My number is bigger')
            elif number < user_num:
                print('My number is smaller')
            else:
                print('You guessed my number!')
                print(f'You have tried {number_of_tries} times to guess my number!')
                choice = input('Do you want to play? ').lower()
                number_of_tries = 0
                number = random.randint(1,11)
        except ValueError:
            print('Type a number!')
            choice = input('Do you want to continue? yes/no ').lower()
    else:
        print('Good bye!')
elif choice == 'no':
    print('Good bye!')
