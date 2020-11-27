#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: November 2020
# this program calculates numbers inserted by user


def main():
    # this program calculates numbers inserted by user

    # input
    first_number = int(input("Enter the first number:"))
    second_number = int(input("Enter the second number:"))

    # process
    total = first_number + second_number

    # output
    print()
    print("{0} + {1} = {2}".format(first_number, second_number, total))


if __name__ == "__main__":
    main()
