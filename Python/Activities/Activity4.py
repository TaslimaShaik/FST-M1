player1=input("Enter player1's name")
player2=input("Enter player2's name")

while True:
    player1_answer=input(player1+" Do you want to choose rock,paper or scissors")
    player2_answer=input(player2+" Do you want to choose rock,paper or scissors")
    if player1_answer==player2_answer:
        print("Tie")
    elif player1_answer=="rock":
        if player2_answer=="scissors":
            print("Rock wins")
        else:
            print("Paper wins")

    elif player1_answer=="scissors":
        if player2_answer=="paper":
            print("scissors wins")
        else:
            print("Rock wins")

    elif player1_answer=="paper":
        if player2_answer=="rock":
            print("paper wins")
        else:
            print("scissors wins")
    else:
        print("Enter valid input")

    repeat=input("Do you want to repeat?")
    if(repeat=="yes"):
        pass
    elif(repeat=="no"):
        raise SystemExit
    else:
        print("Invalid option")
        raise SystemExit