lst = [2,3,4,5,5,2,3,4,4,7]  #temp list
a = []                         #empty list
def uni_ele(lst):
    for i in lst:        # iterate over the lst
        if i not in a:    # conditional statement
            a.append(i)  # append i into empty list
uni_ele(lst)     # function call           
print("the list of unique numbers ",a)  
