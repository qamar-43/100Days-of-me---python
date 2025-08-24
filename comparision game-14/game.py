#create a welcome msg
from data import data
import random
from art import logo, vs
print(logo)




#now to check use if stmt 
def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess =="a"
    else:
        return user_guess == "b"

score = 0
game_should_continue = True
account_b = random.choice(data)


#make the game repeatable
while game_should_continue:
    #using random module to print random account details
    
    #creating variables to store nd print the data by using random module
    account_a = account_b
    account_b = random. choice(data)
    #check if incae, both the acnt details are same or not if its same then generate it 
    


 #creating a function to display account and account detials to compare
    def format_data(account):
        """Takes the account data and returns the printable format."""
        name = account["name"]
        descr = account["description"]
        country = account["country"]
        return f"{name}, a {descr}, from {country}"


    #crating a format to print the data 

    print(logo)
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")






    #let the user make a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #clear the screen
    print("\n" * 5)
    print(logo)

    #check if the user ans is correct
    #- before comparing we need the followers count of each account 
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)



    #comtunue the game is its correct nd track the score
    if is_correct:
        score +=1
        print(f"You're right! current score: {score}")
    else:
        print(f"Sorry you're wromg. Final score {score}")
        game_should_continue = False