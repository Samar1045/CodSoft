import random

def get_user_choice():
    print("\nChoose one : rock, paper, or scissors")
    return input("Your choice:").lower()

def get_computer_choice():
    return random.choice(["rock", "paper",  "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
            (user == "scissors" and computer == "paper") or \
            (user == "paper" and computer == "rock"):
        return "win"
    else:
        return "lose"

def play_game():
    user_score = 0
    computer_score = 0
    print("Welcome to the Rock-Paper-Scissors Game ! ")
    while True:
        user = get_user_choice()
        if user not in ["rock", "paper", "scissors"]:
            print("Invalid input! Try again")
            continue
        computer = get_computer_choice()
        print(f"\n You chose: {user}")
        print(f"\n Computer chose: {computer}")

        result = determine_winner(user, computer)

        if result == "win":
            print("You win this round.")
            user_score += 1
        elif result == "lose":
            print("You lose this round.")
            computer_score += 1
        else:
            print("It's a tie")
        print(f"Score -> You : {user_score} | Computer : {computer_score}")

        play_again = input("\n Do you want to play again? (yes/no) : ").lower()
        if play_again != 'yes':
            print("\n Final Score: ")
            print(f" You: {user_score} | Computer : {computer_score}")
            print("Thanks for playing!")
            break

play_game()