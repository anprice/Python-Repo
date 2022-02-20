#!/usr/bin/env python3

def display_menu():                                                         #Prints the display menu
    print("COMMAND MENU")
    print("list - List all movies")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("exit - Exit program")

def list_movies(movie_list):                                                #Displays the list
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
        return
    else:
        i = 1
        for row in movie_list:
            print(str(i) + ". " + row[0] + " (" + str(row[1]) + ")")
            i += 1
        print
        

def add_movie(movie_list):                                                  #Adds movie to the list
    #initialize local variables/lists

    movie = []
    movie.append(input("Name: "))
    movie.append(input("Year: "))
    movie_list.append(movie)
    print(movie[0] + " (" + movie[1] + ") was added.")
    

def del_movie(movie_list):                                                  #Deletes movie from the list
    num = int(input("Number: "))
    if num < 1 or num  > len(movie_list):                                   #Prints if number is invalid
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(num-1)
        print(movie[0] + " (" + str(movie[1]) + ") was deleted.")
        print()

def main():                                                                 #Main function of the program

    #Initialize variables and lists
    done = False
    movie_list = [["Monty Python and the Holy Grail", 1975], 
                  ["On the Waterfront", 1954], 
                  ["Cat on a Hot Tin Roof", 1939]]

    display_menu()

    while not done:
        command = str(input("Command: "))
        if command.lower() == "list":
            list_movies(movie_list)
        elif command.lower() == "add":
            add_movie(movie_list)
        elif command.lower() == "del":
            del_movie(movie_list)
        else:
            break

if __name__ == "__main__":                                                  #Beginning of the program
    main()
