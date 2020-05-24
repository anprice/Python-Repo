#!/usr/bin/env python3

def display_menu():                                             #Function to display the menu list
    print("COMMAND MENU")
    print("list - List all movies")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("exit - Exit program")

def list_movies(movie_list):                                    #Function to list current movies in the list
    i = 1
    for movie in movie_list:
        print(str(i) + "." + movie )
        i += 1     

def add_movie(movie_list):                                      #Function to add movie to list
    movie_list.append(input("Name: "))
    print(movie_list[-1] + " was added.")

def del_movie(movie_list):                                      #Function to delete movie from list
    num = int(input("Number: "))
    if num < 1 or num  > len(movie_list):
        print("Invalid movie number.\n")
    else:
        rem = movie_list.pop(num-1)
        print(str(rem) + "was deleted.")
        print()

def main():

    done = False
    movie_list = ["Monty Python and the Holy Grail", 
                  "On the Waterfront", 
                  "Cat on a Hot Tin Roof"]
    display_menu()                                              #Calls menu function
    while not done:
        command = str(input("Command: "))
        if command.lower() == "list":
            list_movies(movie_list)
        elif command.lower() == "add":
            add_movie(movie_list)
        elif command.lower() == "del":
            del_movie(movie_list)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command.  Please try again.\n")

if __name__ == "__main__":
    main()
