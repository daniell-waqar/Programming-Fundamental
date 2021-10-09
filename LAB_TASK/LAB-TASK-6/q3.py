d = {1: 100, 2: "abc", 3: True, 4: 40.3, }   #temporary dictionary

def check_key(d, key):    
    for k,v in d.items():   #it will change dictionary into a list of tuple and assign key to k,value to v
        if k == key:    # if key in k
            return True  #then return True
        else:                 #otherwise
            return False   #return False
check_key(d,1)       #function call
