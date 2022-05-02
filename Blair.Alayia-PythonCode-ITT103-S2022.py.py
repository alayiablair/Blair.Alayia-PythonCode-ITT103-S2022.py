#Author: Alayia Blair
#Date Created: April 1, 2022
#Course: ITT103
#Purpose: <A program to calculate and print the commission received by a salesperson>

#Program name: Commission 

#Starting of the program 
'Start'

#Declaring and initalizing variables
Salesperson_num = 0
Sales_amount = 0.0
Class = 0
Salesperson = " "
Commission = 0.0

#Using a Whileloop with a nested if to find Commission of a Salesperson
Salesperson_num = int(input("The number of a salesperson"))
while Salesperson_num != 0:
    Salesperson_num = int(input("The number of a salesperson"))
    Salesperson =(input("Enter name of a salesperson"))
    print (" Salesperson number is",  Salesperson_num, Salesperson)
    Class = int((input("Enter the class of a salesperson")))
    Sales_amount = int((input("Enter the sales amount of a salesperson")))
    if Class == 1:
        if Sales_amount <= 1000:
            print("The commision for ",Salesperson,"is",Sales_amount * 0.6)
        elif (1000 < Sales_amount <= 2000):
           print ("The commision for ",Salesperson,"is",Sales_amount * 0.7)
        else:
           print ("The commision for ",Salesperson,"is",Sales_amount * 0.1)
    elif (Class == 2):
        if Sales_amount < 1000:
           print ("The commision for ",Salesperson,"is",Sales_amount * 0.4)
        else:
            print ("The commision for ",Salesperson,"is",Sales_amount * 0.6)
    elif (Class == 3):
        print ("The commision for ",Salesperson,"is",Sales_amount * 0.045)
    else:
        print(Error)
    t=input("do you wish to continue")
    if t == "no":
        break

#End of program
Stop
