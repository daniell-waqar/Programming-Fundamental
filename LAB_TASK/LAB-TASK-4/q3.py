def fun():
    size = int(input("enter size: "))  #take user input for size
    sym = input("enter symbol: ")      #take user input for symbol
    for i in range(0,size):   # outer loop for number of rows
        for j in range( 0,size-i-1): # inner loop for number spaces
            print(end=" ")
        for j in range(0, i + 1):  # inner loop for number of columns
            print(sym, end=" ")   # printing symbols
        print("")   # ending line after each row

