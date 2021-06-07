#This file will include simple calculator functions such as add, subtract, multiply, and divide

def adder(currentValue):         #Declares a function which will be used to add numbers together and takes in an argument

    #Prompts the user to enter a number and accepts input from the user, typecasts it to a float
    print("Please enter another number for the adder")
    add = float(input())

    #adds the inputted value to the value already stored in the calculator and returns the sum
    sum = currentValue + add
    return sum

def subtractor(currentVaule):
   
    #prompts the user to enter a number and accepts input from the user, typecasts it to a float
    print("Please enter another number for the subtractor")
    subtract = float(input())

    #Takes the difference between the value stored in the calculator and subtract and returns the difference
    difference = currentVaule - subtract
    return difference

def multiplier(currentValue):      #Declares the multiplier function which multiplies two numbers together, takes current value in calculator as an argument

    #prompts the user to enter a number and accepts input from the user, typecasts it to a float
    print("Please enter a number for the multiplier")
    multiple = float(input())

    #Takes the product of the stored value in the calculator and the user inputted number and returns the product
    product = currentValue * multiple
    return product

def divider(currentValue):         #Declares a function divider which divides two numbers and returns the quotient

    #prompts the user to input another number and accepts it, typecasts it to a float
    print("Please enter another number for the divider")
    divide = float(input())

    #Takes the quotient of the stored value in the calculator and the user inputted number and returns the quotient
    quotient = currentValue/divide
    return quotient


def main():            #Declares the main function

    #Prompts the user to enter a number and accepts input from the user
    print("Please enter a number for the calculator")
    currentValue = float(input())

    while(1):            #While loop to keep the calculator running

        #Print Statements describing to the user what the options are
        print("The following options are available")
        print("Option 1: ADD")
        print("Option 2: SUBTRACT")
        print("Option 3: MULTIPLY")
        print("Option 4: DIVIDE")
        print("Option 5: CLEAR")
        print("Option 6: QUIT")

        #Print statement prompting the user to input a number to select an option. Typecasts it to a float
        print("Please enter the number of the option you would like to do")
        userOpt = input()

        #Next will be a series of conditionals to test which option the user selected to perform

        #This will be the first case, if the user selected to do the adder
        if userOpt == '1':

            #performs adder on currentValue and replaces it with the returned sum
            currentValue = adder(currentValue)

            #Displays the sum
            print("The sum is: ", currentValue)

        #This is the second option, in line with the subtractor    
        elif userOpt == '2':

            #performs subtractor on currentValue and replaces it with the difference
            currentValue = subtractor(currentValue)

            #displays the difference
            print("The difference is: ", currentValue)
        
        #This catches option 3, the multiplier
        elif userOpt == '3':

            #performs multiplier on current value and replaces it with the product
            currentValue = multiplier(currentValue)

            #Displays the product
            print("The Product is: ", currentValue)

        #catches option 4, the divider
        elif userOpt == '4':

            #performs divider on currentValue and replaces it with the quotient
            currentValue = divider(currentValue)

            #displays the quotient
            print("The quotient is: ", currentValue)

        #catches option 5, clearing the calculator
        elif userOpt == '5':
            
            #sets the value stored in the calculator to 0 and confirms it to the user
            currentValue = 0
            print("The calculator has been cleared to 0")

        #catches Option 6, quitting, and breaks from the while loop
        elif userOpt == '6':
            break
        
        #catches all other options which are not valid and prints an error message
        else:
            print("That is not a valid option, please enter a valid option")

main()    #calls the main routine