# WorkFlow of Project:

# 1-Input from user (Rock , Paper , Scissors)
# 2- Computer choice (Computer will choose randomly not conditionally)
# 3- Result print

# Cases:

# A - Rock 
# Rock - Rock = Tie
# Rock - Paper = Paper Win
# Rock - Scissor = Rock win

# B - Paper 
# Paper - Ppaer = Tie
# Paper - Rock = Pappper Win
# paper - Scissor = Scissor Win

# C - Scissors
# Scissors - Scissors = Tie
# Scissors - Rock = Rock Win
# Scissors - Paper = Paper Win

import random

item_list = ["Rock", "Paper", "Scissors"]

# Score variables
user_score = 0
computer_score = 0

print("===== Rock Paper Scissors Game =====")

while True:

    user_choice = input("\nEnter Your Move (Rock, Paper, Scissors): ").capitalize()

    # Check invalid input
    if user_choice not in item_list:
        print("Invalid Input! Please choose Rock, Paper, or Scissors.")
        continue

    comp_choice = random.choice(item_list)

    print(f"\nYour Choice = {user_choice}")
    print(f"Computer Choice = {comp_choice}\n")

    # Game Logic
    if user_choice == comp_choice:
        print("Both chose the same = Match Tie!")

    elif user_choice == "Rock":
        if comp_choice == "Paper":
            print("Paper covers Rock = Computer Wins!")
            computer_score += 1
        else:
            print("Rock smashes Scissors = You Win!")
            user_score += 1

    elif user_choice == "Paper":
        if comp_choice == "Rock":
            print("Paper covers Rock = You Win!")
            user_score += 1
        else:
            print("Scissors cuts Paper = Computer Wins!")
            computer_score += 1

    elif user_choice == "Scissors":
        if comp_choice == "Rock":
            print("Rock smashes Scissors = Computer Wins!")
            computer_score += 1
        else:
            print("Scissors cuts Paper = You Win!")
            user_score += 1

    # Display Scores
    print("\n===== SCORE BOARD =====")
    print(f"Your Score     : {user_score}")
    print(f"Computer Score : {computer_score}")

    # Play Again Option
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\n===== FINAL SCORE =====")
        print(f"Your Score     : {user_score}")
        print(f"Computer Score : {computer_score}")

        if user_score > computer_score:
            print("🎉 Congratulations! You are the overall winner!")
        elif computer_score > user_score:
            print("💻 Computer is the overall winner!")
        else:
            print("🤝 The game ended in a tie!")

        print("\nThanks for playing!")
        break