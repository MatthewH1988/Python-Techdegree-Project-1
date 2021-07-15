
import random


def start_game():


    print("Welcome to the Number Guessing Game!")
    
    import random
    
    guess_count = 1
    
    while True:
        try:
            random_number = random.randrange(0, 11)    
            player_guess = int(input("Please guess a number between 0 and 10: "))
            if player_guess < 0 or player_guess > 10:
                raise ValueError
        except ValueError:
            print("That is not a valid response! Please try again!")
            continue
        else:
            while player_guess != random_number:
                if (player_guess > random_number):
                    print("It's lower")
                    guess_count += 1
                    player_guess = int(input("Please guess again!: "))
                elif (player_guess < random_number):
                    print("It's higher")
                    guess_count += 1
                    player_guess = int(input("Please guess again!: "))
                else:
                    attempt_count += 1
                    break
        print("That's correct!")
        break
    
    
    print("That's the end of the game! It took you {} attempts to guess correctly!".format(guess_count))


start_game()