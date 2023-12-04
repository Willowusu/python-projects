# Import the random package to generate random numbers
import random

# Print an introduction message
print("This is a dice simulator")

# Initialize user input to 'y'
user_input = "y"

# Run the dice rolling loop as long as the user enters 'y'
while user_input == "y":
    # Generate a random number between 1 and 6 (inclusive) to simulate a dice roll
    number = random.randint(1, 6)

    # Display the corresponding dice face for the generated number
    if number == 1:
        print("=============")
        print("|           |")
        print("|     o     |")
        print("|           |")
        print("=============")
    elif number == 2:
        print("=============")
        print("|           |")
        print("| o       o |")
        print("|           |")
        print("=============")
    elif number == 3:
        print("=============")
        print("|     o     |")
        print("|     o     |")
        print("|     o     |")
        print("=============")
    elif number == 4:
        print("=============")
        print("| o       o |")
        print("|           |")
        print("| o       o |")
        print("=============")
    elif number == 5:
        print("=============")
        print("| o       o |")
        print("|     o     |")
        print("| o       o |")
        print("=============")
    elif number == 6:
        print("=============")
        print("| o       o |")
        print("| o       o |")
        print("| o       o |")
        print("=============")

    # Prompt the user to roll again or exit
    user_input = input("Press 'y' to roll again any key to exit the program\n")
