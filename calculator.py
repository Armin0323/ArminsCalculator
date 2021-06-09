#This file will include simple calculator functions such as add, subtract, multiply, divide, and some exponents
#All of the strings are formatted {:.4f} when printed to the screen to increase accuracy due to python's emphasis on precision

def adder(currentValue):         #Declares a function which will be used to add numbers together and takes in an argument

    #Prompts the user to enter a number and accepts input from the user, typecasts it to a float
    print("What number would you like to add to {:.4f}?".format(currentValue))
    try:                             #The try statement here is to try to see whether or not there are errors
        add = float(input())

        #adds the inputted value to the value already stored in the calculator and returns the sum
        sum = currentValue + add
        return sum
    except:                          #catches if the user fails to input a number
        print("ERROR: You did not enter a number")        #informs the user they didn't enter a number
        sum = adder(currentValue)     #recursively calls the function to prompt the user again
        return sum                    #returns the correct value as the sum

def subtractor(currentValue):           #delcares subtractor function that takes in the current value stored in the calculator, a user inputted value, and takes the difference
   
    #prompts the user to enter a number and accepts input from the user, typecasts it to a float
    print("What number would you like to subtract from {:.4f}?".format(currentValue))
    try:                                   #this is to try the statement to catch any errors
        subtract = float(input())

        #Takes the difference between the value stored in the calculator and subtract and returns the difference
        difference = currentValue - subtract
        return difference
    except:                                             #catches errors
        print("ERROR You did not enter a number.")      #informs the user of an error
        difference = subtractor(currentValue)           #calls the function recursively and stores the difference
        return difference                               #returns the difference

def multiplier(currentValue):      #Declares the multiplier function which multiplies two numbers together, takes current value in calculator as an argument

    #prompts the user to enter a number and accepts input from the user, typecasts it to a float
    print("What number would you like to multiply to {:.4f}?".format(currentValue))
    try:                                #tries the block of code for errors
        multiple = float(input())       

        #Takes the product of the stored value in the calculator and the user inputted number and returns the product
        product = currentValue * multiple
        return product
    except:                                            #catches errors
        print("ERROR: You did not enter a number.")    #informs the user there was an error
        product = multiplier(currentValue)             #calls the function recursively and stores the product
        return product                                 #returns the product

def divider(currentValue):         #Declares a function divider which divides two numbers and returns the quotient

    #prompts the user to input another number and accepts it, typecasts it to a float
    print("What number would you like to divide {:.4f} by?".format(currentValue))
    try:                                   #tries the block of code for any errors
        divide = float(input())

        #Takes the quotient of the stored value in the calculator and the user inputted number and returns the quotient
        quotient = currentValue/divide
        return quotient
    except:                                                                     #catches any errors
        print("You did not enter a number or you tried to divide by zero.")     #informs the user of errors
        quotient = divider(currentValue)                                        #calls the function recursively and stores the quotient
        return quotient                                                         #returns the quotient

def exponent(currentValue):          #declares an exponent function that takes in the current value stored in the calculator as an argument

    #Print statement to prompt the user for an input, and takes in user input into variable power and casts it as an int
    print("What integer would you like to raise {:.4f} to?".format(currentValue))
    try:
        power = int(input())

        #establishes a counter valuable for the for loop
        counter = 1

        #establishes a temporary value to store the calculations in
        tempValue = currentValue

        #condition that checks if power is 0 in order to return 1 no matter what
        if power == 0:
            return 1

        #condition to check if power is 1, it will return the same value
        elif power == 1:
            return currentValue

        #condition to check if power is less than 0, then it loops and divides the value
        elif power < 0:
            power = abs(power)                   #takes the absolute value of power to find out the range of the for loop
            for x in range(counter - 2,power):       #for loop to iterate through. counter is counter - 2 because there is one extra division to be made and the for loop stops at one minus the magnitude needed
                tempValue = tempValue/currentValue   #stores the iterations in tempValue
            raisedValue = tempValue                 #stores the final value after the for loop iterations in a variable called raisedValue
            return raisedValue           #returns the answer

        #condition to check if power is greater than one, if so it multiplies current value in the forloop.
        elif power > 0:
            for x in range(counter, power):             #for loop for iterations
                tempValue = tempValue * currentValue    #stores every iteration value into tempValue
            raisedValue = tempValue                     #stores the final value after the for loop in a variable called raisedValue
            return raisedValue                          #returns the answer
        else:
            return currentValue                         #returns the value if none of the above are satisfied
    except:                                             #catches an error if the user didn't put in a number
        print("You did not enter an integer.")
        raisedValue = exponent(currentValue)            #calls the function recursively and stores the value in raisedValue
        return raisedValue                              #returns the answer

def initialize():        #The initializer function 
    print("Please enter a number for the calculator: ")     #prompts the user to input a number
    try:                                                    #tries the block of code for any errors
        initValue = float(input())                          #stores the value inputted and typecasts it to a float
        return initValue                                    #returns the value obtained
    except:                                                 #catches any errors
        print("Error, did not enter a number.")             #informs the user of an error
        initValue = initialize()                            #calls the function recursively
        return initValue                                    #returns the value

def main():            #Declares the main function

    #Calls the initialize function to initialize the calculator with an initial value
    currentValue = initialize()

    while(1):            #While loop to keep the calculator running

        #Print Statements describing to the user what the options are
        print("The following options are available:")
        print("Option 1: ADD")
        print("Option 2: SUBTRACT")
        print("Option 3: MULTIPLY")
        print("Option 4: DIVIDE")
        print("Option 5: CLEAR")
        print("Option 6: EXPONENT")
        print("Option 7: QUIT")

        #Print statement prompting the user to input a number to select an option. Typecasts it to a float
        print("Please enter the number of the option you would like to do")
        userOpt = input()

        #Next will be a series of conditionals to test which option the user selected to perform

        #This will be the first case, if the user selected to do the adder
        if userOpt == '1':

            #performs adder on currentValue and replaces it with the returned sum
            currentValue = adder(currentValue)

            #Displays the sum
            print("The sum is: {:.4f}".format(currentValue))

        #This is the second option, in line with the subtractor    
        elif userOpt == '2':

            #performs subtractor on currentValue and replaces it with the difference
            currentValue = subtractor(currentValue)

            #displays the difference
            print("The difference is: {:.4f}" .format(currentValue))
        
        #This catches option 3, the multiplier
        elif userOpt == '3':

            #performs multiplier on current value and replaces it with the product
            currentValue = multiplier(currentValue)

            #Displays the product
            print("The Product is: {:.4f}".format(currentValue))

        #catches option 4, the divider
        elif userOpt == '4':

            #performs divider on currentValue and replaces it with the quotient
            currentValue = divider(currentValue)

            #displays the quotient
            print("The quotient is: {:.4f}".format(currentValue))

        #catches option 5, clearing the calculator
        elif userOpt == '5':
            
            #sets the value stored in the calculator to 0 and confirms it to the user
            currentValue = 0
            print("The calculator has been cleared to 0")
        
        #catches option 6, performing the exponent function
        elif userOpt == '6':

            #takes the value stored in the calculator and passes it to exponent function
            currentValue = exponent(currentValue)
            print("The answer is: {:.4f}".format(currentValue))

        #catches Option 7, quitting, and breaks from the while loop
        elif userOpt == '7':
            break
        
        #catches all other options which are not valid and prints an error message
        else:
            print("That is not a valid option, please enter a valid option")

main()    #calls the main routine
