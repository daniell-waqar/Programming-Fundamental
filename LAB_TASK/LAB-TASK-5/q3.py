def sort_list(l):
    sorted_list = []  # empty list
    while l:    
        maxi = l[0]  #let first number in list is maximum
        for i in l:  # iterate over the list
            if i > maxi: # compare each number with maximum value
                maxi = i  # when value is largest assignt to maxi
        sorted_list.append(maxi) # appending largest value into empty list
        l.remove(maxi)   # remove element from list "l"
    return sorted_list  #return a sorted list
