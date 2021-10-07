total_amount = 0  #initialize
while True:
    ch = input("Press D for Deposite, W for withdraw or Q for quit: ")
    if ch == "D":
        print("how many amount you want to Deposite ?") 
        a = int(input("D:"))  #taking input for Deposite
        total_amount += a   #adding Deposite amount into bank
    elif ch == "W":
        print("how many amount you want to withdraw ?") 
        b = int(input("W:"))   #taking input for Withdraw
        total_amount -= b    #withdraw amount from bank
    else:
        ch == "Q"   
        print("Net Amount",total_amount)
        break
