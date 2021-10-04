n = int(input("enter number: "))  # take input from user 
def fibonacci (n):  
    if n == 1:    # Check if n is 1
        return 1       # then it will return 1
    elif n == 2:    # Check if n is 2
        return 2       # then it will return 2
    elif n > 2 :
        return fibonacci(n-1) + fibonacci (n-2)

for i in range(1,n+1):    #iterate over n
    

    print (i, ':',fibonacci(i))  #printing fibonacci numbers
