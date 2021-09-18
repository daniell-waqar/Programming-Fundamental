char = input("Please Enter the Character : ") #input from user

if(char.isdigit()): # to check is it digit?
    print("it is a Digit")  # if yes then print it
elif(char.isalpha()):   # to check is it alphabet?
    print("it is an Alphabet")  #if yeah then print it
else:      # otherwise
    print("it is a Special Character") #  it is special character
