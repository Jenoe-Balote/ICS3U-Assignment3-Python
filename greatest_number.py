#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on May 2021
# This program determines the greatest of two numbers
#   inputted by the user


def main():
    # this function runs the greatest number program

    # input
    print("Which number is the greatest?")
    number1 = int(input("Enter your first number: "))
    number2 = int(input("Enter your second number: "))
    print("")

    # process and output
    if number1 > number2:
        print("{} is the greater number!".format(number1))
    elif number1 < number2:
        print("{} is the greater number!".format(number2))
    elif number2 == number2:
        print("The two numbers are equal!")


if __name__ == "__main__":
    main()
