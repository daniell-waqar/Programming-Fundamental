# a
directory = "Desktop"   
name = "names.txt"
import os
file = os.path.join(directory,name)     
with open(file,'r') as f:     # Open file for reading
    for i in f:
        print(i[0:4].strip())


# b
directory = "Desktop"    
name = "names.txt"
import os
file = os.path.join(directory,name)
f = open(file,"r")
l = sorted([line.strip() for line in f],key = len)
print("shortest name:",l[0],"length=",len(l[0]))

        
f.close() 

#c
with open(file,'r') as f:
    s = 0
    l = []
    for i in f:
        l.append(i.strip())
    for i in l:
        for j in i:
            s+=1

#d
with open(file,'r') as f:
    s = 0
    l = []
    a = 0
    for i in f:
        l.append(i.strip())
    for i in l:
        a += 1
        for j in i:
            s+=1
    print("Average",s/a)
#e
directory = "Desktop"
name = "names.txt"
name2 = "subj.txt"
l = []
a = 0
import os
file = os.path.join(directory,name)
with open(file,"r") as f:
    for line in f:
        l.append(line.strip())
file2 = os.path.join(directory,name2)
with open(file2,"w") as f:
    for i in range (len(l)):
        f.write(l[a]+" calculus-1,"+"programming fundamental,"+"programming fundamental lab"+"\n")
        a+=1
        

# f
def read_name(n):
    with open(file,'r') as f:
        l = []
        for i in f:
            l.append(i.strip())
            
        for j in l:
            if len(j) == n:
                print(j)


