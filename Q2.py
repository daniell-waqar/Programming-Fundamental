#Q2(b)

z =  []
with open(file,"r")as k:
    l_names = " "
    for line in k:     # Loop over the lines in the file.
        z.append(line.strip().split("\n"))
        if len(line)>len(l_names):    # If the line is longer than l-names
            l_names = line     # Make it our new longest name.
    print(l_names)        #printing L-names
    
  #Q2(a)
  
  l = []
with open(file)as k:
    for li in lst:
        for kh in li:
            print(kh[0:4])
            
    #Q2(c)
    
    
    with open("names.txt", "r") as v:   # Open names_file for reading.
    lengths_sum = 0
    for i in v:
        k = len(i) - 1
        lengths_sum = lengths_sum + k-1 # -1 to account for the newline

print (lengths_sum)


#Q2(d)

with open("names.txt", "r") as c:
    lengths_sum = 0
    n0_names = 0
    for i in c:
       
        lengths_sum= lengths_sum + len(i)  - 1 # -1 to account for the newline
        n0_names =   n0_names + 1
            

print (lengths_sum / len(i)-1)

#Q2(e)

directory = ""   #directory name
name = "names.txt"      #file name
import os           #here we import operating system
file =  os.path.join(directory,name)  
# with open(file)as k: # Open names_file for reading.    
with open(file) as f:
    for line in f:
            name=line.strip()
            names.append(name)
    g=open(khan,'w')
    for line in names:
        g.write(f"{line}    programming fundamental lab, programming fundamental, english composition,calculus-1\n")
    g.close()
    
    
    
 #Q2(g)

khan = []
with open(file) as f:
    for line in f:
            name=line.strip()
            khan.append(name)

name = "Student.txt"
import os
myfile = os.path.join(name)
with open(myfile,"w") as k:
    for line in khan:
        k.write(line+"\n")
 
 

