import random
# print("Winning Rules of the Color choice Game as follows: \nEnter a number from one to five and match computer choice to win...")
computerScore = 0
playerScore = 0
while True:
    print("red = 1\nyellow = 2 \nornage = 3 \ngreen = 4\nblue = 5 \ntake a turn:")
    
    #take input from user
    playerChoice = int(input("Enter a number.."))

    #check for valid input 
    while playerChoice > 5 or playerChoice < 1:
        playerChoice = int(input("Enter a valid number.."))

    #map number to color values
    choices = {1:'red',2:'yellow',3:'orange',4:'green',5:'blue'}

    print("User color choice is..."+choices[playerChoice])
    print("\nNow it's Computers turn to choose a color...")

    computerChoice = random.randint(1,5)

    # while computerChoice == playerChoice:
    #     computerChoice = random.randint(1,5)

    print("\nComputer color choice is..."+choices[computerChoice])

    if(playerChoice == computerChoice):
        playerScore += 1
        print(f" Player Score is {playerScore}")
    else:
        computerScore += 1
        print(f"\nPlayer score:{playerScore} \nComputer Score:{computerScore}")

    print("Do you want to play again ?(Y/N)")
    answer = input()
    if answer.upper() =='N':
        break

if computerScore == playerScore:
    print("Game is a tie")

elif computerScore > playerScore:
    print("You Lost")

elif computerScore < playerScore:
    print("You Won")
print("Thanks for playing!!...")