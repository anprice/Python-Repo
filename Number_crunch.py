#!usr/bin/env python3

import random                                                   #Importing the random module for use

def crunch_numbers(data):                                       #Whatever object is passed as a parameter to crunch_numbers is referenced as a local object named data
    total = 0                                                   #Initializes total to 0
    for number in data:                                         #Iterates through each index in the data object
        total += number                                         #Adding the numbers to the current value of total through each iteration

    average = round(total / len(data))                          #Calculating average by rounding total/number of indexes  
    median_index = len(data) // 2                               #Finding the median by dividing total couunt of indexes by 2
    median = data[median_index]                                 #Storing the value of the median index into variable median
    minimum = min(data)                                         #Minimum in the index list
    maximum = max(data)                                         #Maximum in the index list
    dups = get_duplicates(data)                                 #Invoke get_duplicates function and passes the data object as a parameter, then store returned value in variable dups

    print("Average =", average,
          "Median =", median_index, median,
          "Minimum =", minimum,
          "Maximum =", maximum,
          "Duplicates =", dups)

def get_duplicates(data):                                       #get_duplicates function with data as a parameter
    dups = []                                                   #Initiate an empty list named dups
    for i in range(51):                                         #For loop to iterate starting at 0 to 50 (51)
        count = data.count(i)                                   #Takes the value of i and parses through the data object, then stores the number of occurences of value i in count
        if count >= 2:                                          #If count is greater than 2
            dups.append(i)                                      #Append the value of i in the dups list
    return dups                                                 #Return the list dups

def main():
    fixed_tuple = (0,5,10,15,20,25,30,35,40,45,50)              #Initializes a tuple object named fixed_tuple
    random_list = [0] * len(fixed_tuple)                        #Creates a random_list variable with # of indexes equal to the number in fixed_tuple and are initialized to a value of 0
    for i in range(len(random_list)):                           #Starts for loop to iterate through each index in random_list
        random_list[i] = random.randint(0, 50)                  #Sets each index in random_list to a random number between 0 and 50
    random_list.sort()                                          #Sorts the list in random_list

    print("TUPLE DATA:", fixed_tuple)                           
    crunch_numbers(fixed_tuple)                                 #Pass fixed_tuple to crunch_numbers function
    print()
    print("RANDOM DATA:", random_list)
    crunch_numbers(random_list)                                 #Pass random_list to crunch_numbers function

if __name__ == "__main__":
    main()                                                      #Invokes the main function

