
d = {"one": 1,"two": 2,"three": 3}  #temporary dictionary
def fun(d):
    summ = 0  #initialize
    for k in d:      #iterate over dictionary
        print(k,d[k]) #printing keys and values from dictionary
        summ += (d[k])  #sum of the values in a dictionary assign to summ   
    return summ  # return the summ
v = fun(d)  
print("Sum =",v) 
if v % 2 == 0:     #condition for even
    print("SUM IS EVEN")
else:
    print("SUM IS ODD")

    
