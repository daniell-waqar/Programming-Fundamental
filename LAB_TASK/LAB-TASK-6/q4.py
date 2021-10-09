d={0:0,1:1,2:4,3:1,4:6,5:7}   #temp dictionary
print("printing original dictionary ",d)
for k in d:      #iterate over dictionary
    print("key=",k,"value=",d[k],"\n")#keys and values of a dictionary before multiply with user input                             
a = int(input("Enter a number: "))   #take input from user   
for v in d:    #iterate over dictionary for values
    d[v] = d[v] * a          #multiplying all values of a dictionary with user input
for k,v in d.items():  #it will change dictionary into a list of tuple and assign key to k,value to v
    print(f"key={k},value={v}")  #printing keys and values of a dictionary after multiply with user input

