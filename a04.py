### YOUR CODE FOR openLocks() FUNCTION GOES HERE ###
lockers = []
def openLocks(number_of_students,number_of_lockers):
    if number_of_students == 0 or number_of_lockers == 0:
        return 0
    if number_of_students > 0 or number_of_lockers > 0:
        return None
    for i in range(number_of_lockers):
        lockers.append(0)
    for j in range(number_of_students):     
        if j == 0 :
            for i in range(number_of_lockers):
                lockers[i] = 1
        if j == 1:
            for k in range(1,number_of_lockers,j+1):
                lockers[k] = 0
        if j > 1:
            for l in range(j,number_of_lockers,j+1):
                if lockers[l] == 1:
                    lockers[l] = 0
                else:
                    lockers[l] = 1    
    counter = 0
    for i in range(0,number_of_lockers):
            if lockers[i] == 1:
                counter = counter+1        
    return counter


### YOUR CODE FOR mostTouchableLocker() FUNCTION GOES HERE ###
def mostTouchableLocker(number_of_students,number_of_lockers):
    if number_of_students == 0 or number_of_lockers == 0:
        return 0
    if number_of_students < 0 or number_of_lockers < 0:
        return None
    for i in range(number_of_lockers):
        lockers.append(0)
    for j in range(number_of_students):     
        if j == 0 :
            for i in range(number_of_lockers):
                lockers[i] = 1
        if j == 1:
            for k in range(1,number_of_lockers,j+1):
                lockers[k] = lockers[k] + 1
        if j > 1:
            for l in range(j,number_of_lockers,j+1):
                if lockers[l] ==  1:
                    lockers[l] = lockers[l] + 1
                else:
                    lockers[l] =lockers[l] +1  
    counter = 0
    min_to_max = 0
    for i in range(0,number_of_lockers):
        if lockers[i] >= min_to_max:
            min_to_max = lockers[i]
            counter = i+1
    return counter


#### End OF MARKER

