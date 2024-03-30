from art import logo
from random import randint

def game():
    print(logo)
    def set_level(level_input):
        if level_input.lower() == 'easy':
            return 9
        else:
            return 4
            
    def start_again(new_game):
        if new_game.lower() == 'y':
            return True
        else:
            print('Thanks for playing Guess-O-Tron!')
            GAME_OVER = True
            return False
        
    level_input = input('choose your level "easy" or "hard" :').lower()

    if level_input == 'easy' or level_input == 'hard':
        pass
    else:
        level_input = input('your answer does not match "easy" or "hard" please choose again :')
    lives = set_level(level_input)

    guess = int(input(f'Guess a number between 1 and 100 :'))
    def get_random():
        return randint(1,100)
    
    number = get_random()
    GAME_OVER = False

    while lives > 0 and GAME_OVER == False:
        if guess == number:
            new_game = input(f'Congratulations the number is indeed {guess} You Win! Would you like to try again (Y/N)? :')
            if start_again(new_game):
                game()

        elif guess > number:
            guess = int(input(f'{guess} is too high try again :'))
            lives -= 1
        else:
            guess = int(input(f'{guess} is too low try again :'))
            lives -= 1
    
    if lives == 0:
        new_game = input('Sorry, you are out of guesses, would you like to play again (Y/N)? :')
        if start_again(new_game):
            game()
        else:
            GAME_OVER = True


game()