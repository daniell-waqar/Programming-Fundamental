#a
a = [1,3,5]
print("The list a ",a)
b = [2,4,6]
print("The list b",b)
c = a + b
print("The new list c after adding list a and list b is ",c)

#b
def max_list(c):
    max_val = None   #let maximum value is none
    for i in c:    #iterate through the list c
        if (max_val is None  or i > max_val):   #compare each number with max_val
            max_val = i    
    return  max_val   #return the max_value
#c

c.insert(3,42) #inserting 42 as a fourth element 
print(c)   #print new list c after adding 42

#d
c.append(7) # appending 7 8 9 at the end of c
c.append(8)
c.append(9)
print(c)    #print new list c after adding 7 8 9

#e
print("the first two element of list c is ",c[:2])

#f
print("the last element in list b is ",b[-1])

#g
print("the length of a is ",len(a))
