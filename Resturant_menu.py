Burger = [
    ['Zinger Burger', 230],
    ['Zinger Cheese Burger', 260],
    ['Beef Burger', 250],
    ['thames special burger', 320],
    ['tower burger', 400],
    ['fish burger', 350],
    ['fish cheese burger', 380],
    ['shami burger', 120]
    
    
]

Pizza = [
    ['Pan Pizza', 650],
    ['Thin Crust Pizza', 650],
    ['Wood-Fired Artisan Pizza', 650],
    ['Meat Pizza',700],
    ['BBQ Chicken Pizza',850]
]

options = []
while True:
    print('\nMenu\n')
    print('Select what do you want\n\n1.Burger Menu\n\n2.Pizza Menu\n\n3.Total Bill\n')
    print('select 1 or 2 : ')
    option = input()
    if option == '1':
        count = 0
        number = []
        for item in Burger:
            count += 1
            number.append(count)
            print(f'{count}. {item[0]} - price {item[1]}')
        option2 = input('Plz select your burger (No.): ')
        qauntity = input('Enter the number of quantity (No.): ')
        options.append([Burger[int(option2) - 1][0], Burger[int(option2) - 1][1], int(qauntity)])
    
    if option == '2':
        count = 0
        number = []
        for item in Pizza:
            count += 1
            number.append(count)
            print(f'{count}. {item[0]} - price {item[1]}')
        option2 = input('Plz select your Pizza (No.): ')
        qauntity = input('Enter the number of quantity (No.): ')
        options.append([Pizza[int(option2) - 1][0], Pizza[int(option2) - 1][1], int(qauntity)])
    
    if option == '3':
        count = -1
        totalcount = []
        for k in options:
            count += 1
            print(f'{options[count][0]} - price {options[count][1]} {options[count][2]}x [total: {options[count][1] * options[count][2]}]')
            totalcount.append(int(options[count][1]) * int(options[count][2]))
        print(f'total bill: {sum(totalcount)}')
        with open('bill.txt', 'w+') as l:
            l.write(str(sum(totalcount)))
            l.close()
    again = input("Do you want the bill [yes/no] ")
    if again == "no":
        break
