import random
print("welcome to roock paper scissor")

# ROCK = ('''  
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# ''')



















while True:
    
    user = input("chose any of them: ROCK,PAPER,SCISSOR:")
    print("YOU CHOSE",user)
    
    computer=random.choice(["ROCK","PAPER","SCISSOR"])
    print("the  computer choice is:",computer)
    
    if user == computer:
        print(" its a tie, try one moore time")
        
        
    elif user == "PAPER":
        if computer=="ROCK":
             print("computer lose, you win")
             break
        else:
            print("you lose")
            break
            
    elif user ==" ROCK":
        if computer=="PAPER":
             print("computer lose, you win")
             break
        else:
            print("you lose")
            break
            
    elif user == "SCISSOR":
        if computer=="ROCK":
             print("computer lose, you win")
             break
        else:
            print("you lose")
            break
    
    else:
        print("worng input")

print("THANKS FOR PLAYING")
    
