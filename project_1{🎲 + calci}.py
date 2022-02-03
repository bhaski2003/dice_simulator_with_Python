import random
print("I WELCOME!! YOU TO THE DICE ROLLING SIMULATOR SESSION!!")

Bhask_asks = input("Bhask_asks - want to roll a dice ? (y/n/Y/N)")

while(Bhask_asks == 'y' or 'Y'):

    num = random.randint(1,6)

    if num == 1:
        print("generated random numb is",num)
        print("[-----]:")
        print("[     ]:")
        print("[  O  ]:")
        print("[     ]:")
        print("[-----]:")


    elif num == 2:
        print("generated random numb is",num)
        print("{-----}:")
        print("{O    }:")
        print("{     }:")
        print("{    O}:")
        print("{-----}:")


    elif num == 3:
        print("generated random numb is",num)
        print("{-----}:")
        print("{O    }:")
        print("{  O  }:")
        print("{    O}:")
        print("{-----}:")


    elif num == 4:
        print("generated random numb is",num)
        print("{-----}:")
        print("{O   O}:")
        print("{     }:")
        print("{O   O}:")
        print("{-----}:")


    elif num == 5:
        print("generated random numb is",num)
        print("{-----}:")
        print("{O   O}:")
        print("{  O  }:")
        print("{0   O}:")
        print("{-----}:")


    else:
        print("generated random numb is",num)
        print("{-----}:")
        print("{O O O}:")
        print("{     }:")
        print("{O O O}:")
        print("{-----}:")

    Bhask_says = input("Bhask_says - press y to continue and n to exit. (y/n/Y/N)")


    if Bhask_says == 'n' or 'Y':
        print("Bhask_says = Thank you for participating!!")
        exit()
        



#calci


num_1 = int(input("Enter your first number"))
num_2 = int(input("Enter your second number"))

operation = input("enter the operation to be done : (+ , -, * , / , % , // , ** )")


if operation == '+' :
    print(num_1 + num_2)


elif operation == '-' :
    print(num_1 - num_2)


elif operation == '*' :
    print(num_1 * num_2)


elif operation == '/' :
    print(num_1 / num_2)


elif operation == '%' :
    print(num_1 % num_2)


elif operation == '//' :
    print(num_1 // num_2)


elif operation == '**' :
    print(num_1 ** num_2)





























