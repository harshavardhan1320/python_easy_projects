import random
game=["rock","paper","scissors"]
choosen=int(input("what do u choose ? type 0 for rock, 1 for paper, 2 for scissors "))
if choosen > 2:
    print("please enter a valied input ;)")
else:
    your_choise=game[choosen]

    print(f"your choise is {your_choise}")



    computer=random.randint(0,2)
    computer_choise=game[computer]
    print(f"the computer has choosen {computer_choise}")
    if your_choise==computer_choise:
        print("game is tie")
    elif your_choise=="rock" and computer_choise=="paper":
        print("computer won the game")
    elif your_choise=="rock" and computer_choise=="scissors":
        print("you won the game")  
    elif your_choise=="paper" and computer_choise=="rock":
        print("you won the game")  
    elif your_choise=="paper"and computer_choise=="scissors":
        print("computer won the game")
    elif your_choise=="scissors" and computer_choise=="paper":
        print("you won the game")
    elif your_choise=="scissors" and computer_choise=="rock":
        print("computer won the game")
    else:
        print("please restart the game ")

