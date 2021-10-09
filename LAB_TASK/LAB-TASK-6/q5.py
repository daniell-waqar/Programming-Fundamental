d={0:0,1:1,2:4,3:1,4:6,5:7}  #temp dictionary
def max_min(d): #function that find max and min value in a dictionary
    l = []   #empty list
    max = 0  #asssume initially maximum and minimum is zero
    min = 0 
    for v in d.values():  #values is a function that will return values from dictionary
        l.append(v)     #append values into empty list
        l.sort()     #then sort the list
        max=l[-1]    
        min= l[0]
    return(max,min)     #return the maximum value "max" and minimum value "min"
print(max_min({0:0,1:1,2:4,3:1,4:6,5:7}))  #function call
