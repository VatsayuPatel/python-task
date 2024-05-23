import random

print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    choice = int(input("Enter your choice :"))

    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please '))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    # print user choice
    print(f'User choice is {choice_name}')
    print('\nNow its Computers Turn....')

    # Computer chooses randomly any number among 1 , 2 and 3. Using randint method of random module
    comp_choice = random.randint(1, 3)

    # looping until comp_choice value is equal to the choice value
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'

    print(f"Computer choice is {comp_choice_name}\n")
    print(choice_name, 'Vs', comp_choice_name)

    if choice == comp_choice:
        print('Its a Tie')
        result = "Tie"

    # condition for Paper  winning
    if choice == 1 and comp_choice == 2:
        print('paper wins')
        result = 'paper'
    elif choice == 2 and comp_choice == 1:
        print('paper wins')
        result = 'Paper'

    # condition for Rock  winning
    if choice == 1 and comp_choice == 3:
        print('Rock wins')
        result = 'Rock'
    elif choice == 3 and comp_choice == 1:
        print('Rock wins')
        result = 'rock'

    # condition for Scissor winning
    if choice == 2 and comp_choice == 3:
        print('Scissors wins')
        result = 'scissor'
    elif choice == 3 and comp_choice == 2:
        print('Scissors wins')
        result = 'scissor'

    # Printing either user or computer wins or Tie
    if result == 'Tie':
        print("Its a tie...!")
    if result == choice_name:
        print("User wins...!")
    else:
        print("Computer wins...!")

    print("\nDo you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break

print("Thanks for playing...!")
