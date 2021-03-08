# import python random module
import random

# display title() function
def display_title():
    print('Welcome to guess the number game v1.2 \n')

# play game() function. 
def play_game():
    # generate random number between 1 and 10
    return random.randint(1, 10)

# main() function for starting the game
def main():
    # call display title function
    display_title()
    # call play_game() function to generate a random number between 1 and 10
    random_number = play_game()
    # start a user input
    user_input_01 = input("Please guess a number between 1 and 10 \n")
    # start a while loop. this loop will continue until user enters a correct number
    if user_input_01.isdigit() == True:
        while (int(user_input_01) != random_number):
            if (int(user_input_01) < random_number):
                # if user input is smaller than the random number, display 'Too low' message any start new input prompt
                user_input_01 = input("Too low \n")
            if (int(user_input_01) > random_number):
                # if user input is greater than the random number, display 'Too high' message any start new input prompt
                user_input_01 = input("Too high \n")
        else:
            # If the user guess matches the random number display the message, 'You guessed it '
            print('You guessed it \n')
            display_title()
            # create a variable with value "yes"
            play_again = "yes"
            # generate 2nd random number for the game
            random_number_02 = play_game()
            # ask if user wants to play the game again
            user_answer = str(input("Do you want to play the game again? answer yes or no \n"))
            # check if user's answer is 'yes' stored in 'play_again' variable
            if (user_answer == play_again):
                # start a while loop. this loop will continue until user enters a correct number
                main()
            else:
                # if user enters 'no' or something else, finish the loop and show message 'See you again'
                print('See you again')
    else:
        print('Error! you have to enter an integer')

# call the main function
main()