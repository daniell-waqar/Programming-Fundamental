x = int(input())    # taking two inputs from user
y = int(input())
if x > 0 and y > 0:  # if both inputs are greater than zero  print it
    print((x,y),"point lies in first quadrant")
elif x < 0 and y > 0: # if 1st input is less than zero other is greater print it
    print((x,y),"point lies in second quadrant")
elif x < 0 and y < 0: # if both inputs are less than zero  print it
     print((x,y),"point lies in third quadrant")
elif x > 0 and y < 0:  # if 1st input is greater than zero other is less print it
     print((x,y),"point lies in fourth quadrant")
    
