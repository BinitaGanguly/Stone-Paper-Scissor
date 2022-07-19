import random

while True:
    choices=["Stone","Paper","Scissor"]
    print("\t\t\t|| STONE,PAPER & SCISSOR ||\n")
    computer = random.choice(choices)
    player = None
    #print("computer choose: ",computer)
    while player not in choices:
        player=input("Hello player! enter Stone,Paper or Sicssor:\n")
        

        if player == computer:
            print("Player:",player)
            print("Computer:",computer)
            print("The game is Tie")

        elif player == "Stone":
            if computer == "Scissor":
                print("Player:",player)
                print("Computer:",computer)
                print("Player WINS")
            if computer == "Paper":
                print("Player:",player)
                print("Computer:",computer)
                print("Computer WINS")

        elif player == "Paper":
            if computer == "Stone":
                print("Player:",player)
                print("Computer:",computer)
                print("Player WINS")
            if computer == "Scissor":
                print("Player:",player)
                print("Computer:",computer)
                print("Computer WINS")

        elif player == "Scissor":
            if computer == "Stone":
                print("Player:",player)
                print("Computer:",computer)
                print("Computer WINS")
            if computer == "Scissor":
                print("Player:",player)
                print("Computer:",computer)
                print("Player WINS")
        else:
            print("Wrong Input");
    playagain=input("Want to play again?\nPress (Yes/No) : ")
    if playagain!= "Yes":
        break
print("Thank You for playing.")


