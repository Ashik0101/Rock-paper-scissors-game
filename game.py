import random

# define function to get user choise
def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock,paper,scissors) : ").lower()
        if user_choice in ["rock","paper","scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please enter correct option.")




# get computer's choice
def get_computer_choice():
    choices = ['rock','paper','scissors']
    return random.choice(choices)


# determine winner based on the conditions
def determine_winner(user_choice,computer_choice):
    """ compare the user's choice and computer's choice and determine the winner """
    if user_choice == computer_choice:
        return "draw"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"
    else:
        return "computer"
    


# define function for playing game
def play_game():
    user_score = 0
    computer_score = 0
    draw = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("Computer's choice:",computer_choice)


        winner = determine_winner(user_choice,computer_choice)
        
        if winner == "user":
            user_score += 1
            print("You win!")
        elif winner == "computer":
            computer_score += 1
            print("Computer wins!")
        else:
            draw += 1
            print("It's a draw!")     
        print('Score: User -',user_score, "Computer -",computer_score, "Draw -",draw)   
        print()    
        play_again = input("Do you want to play again?(yes/no) : ").lower()
        if play_again != "yes":
            break
        

print("Let's play rock, paper and scissors!")
play_game()