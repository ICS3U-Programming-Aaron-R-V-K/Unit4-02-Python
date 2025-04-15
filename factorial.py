# !/usr/bin/env python3
# Created By: Aaron Rivelino
# Date: April 14, 2025
# Is a do...while program
# It gets the number from the use and adds + 1 from 0 to the user number
# Then it multiplies all the numbers(factorial)


def main():
    # Set counter to 0 (used for counting up to the number)
    counter = 0
    # Set product to 1 (this will store the factorial result)
    product = 1

    # Get user input as a string
    user_number = input("Enter a whole number: ")
    try:

        # Validate that the number is an integer
        number = int(user_number)
        # Check if the entered number is negative
        if number < 0:
            # If the number is negative, print a error message
            print("Please enter a non-negative number.")
        elif number == 0:
            # Factorial of 0 is 1 by definition
            product = 1
        else:
            # Use while true to simulate a do.. while statement
            while True:
                # Add + 1 to counter so it starts from 0 to the user num
                counter = counter + 1
                # Multiply the current product by the counter to calculate factorial
                product = product * counter
                # Check if it has reach the number so that it stops
                if counter == number:
                    # If it reached the number it breaks or ends the loop
                    break

        # After it prints the factorial
        print(f"The factorial of {number} is {product}")

    # Exception for any invalid inputs
    except Exception:
        # Print an error message if the user does not enter a valid whole number
        print("Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    main()
