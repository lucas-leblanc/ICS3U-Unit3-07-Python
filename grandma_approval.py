#!/usr/bin/env python3

# Created by: Lucas LeBlanc
# Created on: Oct 2022
# This program uses a compound boolean statement


def main():
    # This function determines if the user will be approved

    # Input
    user_age = input("Enter your age: ")
    print("")

    # Process and Output
    try:
        user_age_number = int(user_age)
        if user_age_number > 40:
            print("You are too old for my grandchild.")
        elif user_age_number < 25:
            print("You are too young for my grandchild.")
        else:
            print("You are right for my grandchild.")

    except Exception:
        print("Invalid input.")

    print("\nDone")


if __name__ == "__main__":
    main()
