from random import randint
from art import logo

def display_logo():
    print(logo)
    
#creating global variables
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5






#function to check the user guess against the computer guesss
def check_answer(user_guess, actual_ans, turns):
    if user_guess > actual_ans:
        print("Answer is Too Low!!")
        return turns - 1
    elif user_guess < actual_ans:
        print("Answer is Too High!!")
        return turns - 1
    else :
        print(f"You Got it!!! The Answer was {actual_ans}")




#function to set the diifficulty level i.e. easy or hard
def set_difficulty():
    level = input("Choose a Difficulty level . Type 'Easy' or 'Hard'")
    if level == "easy": 
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS




def game():
    # choosinng a random no. from 1- 100
    print("lets START the Number Guessing  game!!!!")
    print("Guess a number between 1 and 100")
    answer = randint(1, 100)


    turns = set_difficulty()
    #creating a while loop to check the level nf give attempts accordingly
    guess = 0
    while  guess != answer:
        print(f"You have {turns} attempt remaining to guess the correct number.")
        #leting the user choose s no.
       
        guess = int(input("Make a Guess: "))
        

        #calling the check_ans func to check the ans ns continue tha game
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of od guesses, you lose!")
            print(f"The correct anwer was {answer}.")
            return
        elif guess != answer:
            print("Guess again!")

game()















