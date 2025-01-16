import random

def game():
    print("Welcome to Old days")
    print("Instruction : Type 'rock','paper',or'scissors' to play. Type 'quit' to top the game.")

    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter your choice (rock,paper,scissors):") .lower()

        if user_choice == 'quit' :
            print("Out of game!")
            print(f"Final Scores - You: {user_scores}, Computer: {computer_score}")
            break

        if user_choice not in ['rock' , 'paper','scissors']:
            print("Invalid choice! Please try again.")
            continue

        computer_choice = random.choice(['rock','paper','scissors'])
        print(f"Computer chose:{computer_choice}")

        if user_choice == computer_choice:
            print("TIE")
        elif(user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'scissors' and computer_choice == 'paper')or\
            (user_choice == 'paper' and computer_choice == 'rock'):
            print("YOU WIN")
            user_score +=1
        else:
            print("LOSE!")
            computer_score +=1
        
        print(f"score - You: {user_score}, Computer: {computer_score}")
        print()
game()