import random

print("Welcome to ROCK PAPER SCISSORS")
print("__"*16)

while True:
    rps = ["Rock", "Paper", "Scissors"]
    computer = random.choice(rps)
    print("\nSELECT 1 FOR ROCK, 2 FOR PAPER, 3 FOR SCISSORS")
    player = int(input('Enter your choice (or 0 to quit): '))

    if player == 0:
        print("Thank you for playing!")
        break

    if player not in [1, 2, 3]:
        print("Invalid choice. Please choose again.")
        continue

    print("Computer Chose: ", computer)

    if computer == "Rock":
        if player == 1:
            print("It's a tie!")
        elif player == 2:
            print("Player Wins!")
        elif player == 3:
            print("Computer Wins!")
   
    elif computer == "Paper":
        if player == 1:
            print("Computer Wins!")
        elif player == 2:
            print("It's a tie!")
        elif player == 3:
            print("Player Wins!")
    
    elif computer == "Scissors":
        if player == 1:
            print("Player Wins!")
        elif player == 2:
            print("Computer Wins!")
        elif player == 3:
            print("It's a tie!")