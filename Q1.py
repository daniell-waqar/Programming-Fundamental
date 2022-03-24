def fun1(dic):
    counter = 0
    for i in dic:
        print(i,"=",dic[i])
        counter += 1
    print("The sum of items is :",counter)
    if counter % 2 == 0:
        print("SUM IS EVEN !")
    elif counter % 2 != 0:
        print("SUM IS ODD !")
