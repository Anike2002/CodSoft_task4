import random
print("Welcome to the Rock Paper Scissors Game\n")

print("Game winning rules are :")
print("Rock vs Paper = Paper \n"
      "Paper vs Scissors = Scissors \n"
      "Rock vs Scissors = Rock\n")

user_score = 0
computer_score = 0
tie = 0

choice1 = "Rock"
print('1',choice1)
choice2 = "Paper"
print('2',choice2)
choice3 = "Scissors"
print('3',choice3)

while True:
    user_choice = int(input("Enter a user choice"))

    if user_choice == 1:
        user_choice = "Rock"
        print("User choose ",user_choice)
    elif user_choice == 2:
        user_choice = "Paper"
        print("User choose ",user_choice)
    elif user_choice == 3:
        user_choice = "Scissors"
        print("User choose ",user_choice)
    else:
        print("Choose invalid choice ")

    choices = ("Rock","Paper","Scissors")
    computer_choice = random.choice(choices)

    if computer_choice == "Rock":
       print("computer choose","Rock")
    elif computer_choice == "Paper":
       print("computer choose","Paper")
    else :
        computer_choice == "Scissors"
        print("computer choose","Scissors")

    if user_choice == computer_choice:
        print("It's a tie")
        tie = tie + 1
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        print("User win")
        user_score = user_score + 1
    else:
        print("Computer win")  
        computer_score = computer_score + 1

    Score = "score: User:{}, Computer:{}, Tie:{}"
    print(Score.format(user_score , computer_score , tie))

    play_again = input("Do you want play again? (yes/no) :")
    if play_again != 'yes':
      print("Thanks for playng")
      break