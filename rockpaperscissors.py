import random
def choose_option():
    choice = input("Choose Rock,Paper or Scissors: ")
    if choice in ["rock", "r"]:
        return "r"
    elif choice in ["paper", "p"]:
        return "p"
    elif choice in ["scissors", "s"]:
        return "s"
    else:
        print("Invalid choice")
        return None
def comp_option():
    c_choice_int = random.randint(1,3)
    if c_choice_int == 1:
        return "r"
    elif c_choice_int == 2:
        return "p"
    else:
        return "s"
    
def determine_winner(choice,c_choice,player_wins,comp_wins):
    if (choice == "r" and c_choice == "p") or \
       (choice == "s" and c_choice == "r") or \
       (choice == "p" and c_choice == "s"):
        print(f"You chose {choice} and the computer chose {c_choice}. You lose.")
        return player_wins, comp_wins + 1
    elif choice == c_choice:
        print("It's a tie.")
        return player_wins, comp_wins
    else:
        print(f"You chose {choice} and the computer chose {c_choice}. You win!")
        return player_wins + 1, comp_wins
def main():
    player_wins=0
    comp_wins=0
    while True:
        print("Player wins:", player_wins)
        print("Comp wins:", comp_wins)
        user_choice=choose_option()
        comp_choice=comp_option()
        player_wins,comp_wins=determine_winner(user_choice,comp_choice,player_wins,comp_wins)
        my_choice = input("Do you want to play again?")
        if my_choice != "yes" or my_choice != "y":
            print("Thankyou for playing")
main()
