while True:
    a = input("Enter first player name: ")
    b = input("Enter second player name: ")
    x = input(a + " do You want to choose rock,paper or scissor?")
    y = input(b + " do You want to choose rock,paper or scissor?")
    if x == y:
        print("It's a tie!")
        
    elif x == "rock" and  y == "scissor":
        print("Rock beats scissor!",a, "You win!")
        
    elif x == "rock" and y == "paper":
        print("Paper beats rock!",a, "You loss,")
        
    elif x == "scissor" and  y == "paper":
        print("Scissor beats paper!",a, "You win!")
        
    elif x == "scissor" and  y == "rock":
        print("Rock beats scissor!",a, "You loss.") 
        
    elif x == "paper" and  y == "rock":
        print("Paper beats rock!",a, "You win!")
    
    elif x == "paper" and y == "scissor":
        print("Scissor beats paper!",a, "You loss.")
            
    
    z = input("Do You want to play again?(Y/N)")
    if z == "N" or z == "n":
        break
