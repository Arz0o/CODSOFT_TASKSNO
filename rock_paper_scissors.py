import random

print("=" * 40)
print("      ROCK PAPER SCISSORS GAME")
print("=" * 40)

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0
ties = 0

while True:
    print("\nChoose an option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_input = input("Enter your choice (1/2/3): ")

    if user_input not in ["1", "2", "3"]:
        print("Invalid choice! Please enter 1, 2, or 3.")
        continue

    user_choice = choices[int(user_input) - 1]
    computer_choice = random.choice(choices)

    print("\nYour choice     :", user_choice.capitalize())
    print("Computer choice :", computer_choice.capitalize())

    if user_choice == computer_choice:
        print("Result          : It's a Tie!")
        ties += 1

    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or
        (user_choice == "paper" and computer_choice == "rock")
        or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Result          : You Win!")
        user_score += 1

    else:
        print("Result          : Computer Wins!")
        computer_score += 1

    print("\n----------------------------------------")
    print("Your Score     :", user_score)
    print("Computer Score :", computer_score)
    print("Ties           :", ties)
    print("----------------------------------------")

    play_again = input("\nDo you want to play again? (y/n): ").lower()

    if play_again != "y":
        print("\nThank you for playing!")
        print("Final Score:")
        print("You:", user_score)
        print("Computer:", computer_score)
        print("Ties:", ties)
        break