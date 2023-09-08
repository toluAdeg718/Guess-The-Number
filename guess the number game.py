import random


EASY_NUMBER_TURNS = 10
HARD_NUMBER_TURNS = 5

def check_answer(guess, answer,turns):
    if guess < answer:
        print("Too low, Try again")
        return turns - 1
    elif guess > answer:
        print("Too High, Try again")
        return turns - 1
    else:
        print(f"You guessed the correct number, the {answer}")

def set_difficulty():
    chosen_level = input("Choose the difficulty level:'easy' or 'hard': ")
    if chosen_level == 'easy':
        return EASY_NUMBER_TURNS
    else:
        return HARD_NUMBER_TURNS



def game():
    print("Welcome the guessing game")
    print("I'm guessing of a number between 1 and 100")
    answer = random.randint(1,100)
    turns = set_difficulty()

    while turns > 0:
        guess = int(input("Make your guess:"))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print(f"You have run out of guesses,you lose.The correct number is {answer}")
            break
        elif guess == answer:
            break
        else:
            print(f"Guess again, You have {turns} guesses left")

play_again = 'y'
while play_again.lower() == 'y':
    game()
    play_again = input("Do you want to play again? ")


game()
