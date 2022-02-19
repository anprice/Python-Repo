#!/usr/bin/env python3

def calculate_future_value(monthly_investment, yearly_interest, years):                                                     #Defines calculate_future_value and uses passed parameters for local variables
    
    monthly_interest_rate = yearly_interest / 12 / 100                                                                      #Stores interest rate calculation
    months = years * 12                                                                                                     #Stores months

    future_value = 0.0
    for i in range(0, months):                                                                                              #Starts for loop starting at 0 ending at value of months
        future_value += monthly_investment                                                                                  #Adds value of monthly_investment to future_value in each loop iteration
        monthly_interest = future_value * monthly_interest_rate                                                             #Stores calculated value in monthly_interest per iteration
        future_value += monthly_interest                                                                                    #Stores calculated future_value per iteration
    
    return future_value                                                                                                     

def get_float():
    min = 0
    max = 1000
    while True:
        monthly_investment = float(input("Enter monthly investment:\t"))                                                    #Stores users input value and typecasts it to float so it can be used in a formula later on 
        if monthly_investment > min and monthly_investment <= max:                                                          #Condition to break the loop
            break   
        else:
            print("Entry must be greater than ", min, " and less than or equal to", max ,".")                              #Continue loop until valid input is inserted
            continue                                                                                                        #Starts loop over
    
    low = 0
    high = 15
    while True:
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))                                                #Stores users input value and typecasts it to float so it can be used in a formula later on
        if yearly_interest_rate > low and yearly_interest_rate <= high:                                                     #Condition to break the loop
            break
        else:
            print("Entry must be greater than ", low, " and less than or equal to", high, ".")                             #Continue loop until valid input is inserted
            continue                                                                                                        #Starts loop over

    return monthly_investment, yearly_interest_rate

def get_int():                                                                                                              
    min = 0                                                                                                                 
    max = 50                                                                                                                
    while True:                                                                                                             
        years = int(input("Enter number of years:\t\t"))                                                                    #Stores users input value and typecasts it to an int so it can be used in a formula later on
        if years > min and years <= max:                                                                                    #Condition to break the loop
            break                                                                                               
        else:                                                                                                               #Continues loop until valid input is inserted
            print("Entry must be greater than ", min, " and less than or equal to", max, ".")
            continue

    return years                                                                                                            #Returns number of years

def main():
    choice = "y"                                                                                                            #Sets choice to value of y for loop
    while choice.lower() == "y":                                                                                            #Continues loop while choice == y
        
        monthly_investment, yearly_interest_rate = get_float()                                                              #Setting monthly_investment and yearly_interest_rate values by the returned values of the get_float function
        years = get_int()                                                                                                   #Setting the value of years to the return value of get_int function

        
        future_value = calculate_future_value(monthly_investment, yearly_interest_rate, years)                              #Setting the value of future_value by the return value of calculate_future_value which passes 3 parameters

        print("Future value:\t\t\t" + str(round(future_value, 2)))                                                          #Typecasting future_value to a string
        print()

        choice = input("Continue? (y/n): ")                                                                                 #Pass user input to input function and set value to choice
        print()

    print("Bye!")

if __name__ == "__main__":
    main()                                                                                                                  #Invokes main function

