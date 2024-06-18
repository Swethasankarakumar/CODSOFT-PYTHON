import random
def get_user_choice():
    user_choice = input("Choose rock, paper, or scissors: ")
    return user_choice
def get_computer_choice():
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    return computer_choice
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'rock' and computer_choice == 'scissors':
        return "You win!"
    elif user_choice == 'scissors' and computer_choice == 'paper':
        return "You win!"
    elif user_choice == 'paper' and computer_choice == 'rock':
        return "You win!"
    else:
        return "Computer wins!"
def play_again():
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again == 'yes':
        return True
    else:
        return False
user_score = 0
computer_score = 0

while True:
    print("Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose {user_choice}, computer chose {computer_choice}.")
    print(determine_winner(user_choice, computer_choice))

    #update scores
    if determine_winner(user_choice, computer_choice) == "You win!":
        user_score += 1
    elif determine_winner(user_choice, computer_choice) == "Computer wins!":
        computer_score += 1

    # Display scores
    print(f"Your score: {user_score}")
    print(f"Computer score: {computer_score}")

    # Ask to play again
    if not play_again():
        break

print("Thanks for playing!")
