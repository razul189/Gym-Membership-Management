# lib/cli.py

from helpers import (
    exit_program,
    member_sign_up,
    get_all_members
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            member_sign_up()
        elif choice == "2":
            get_all_members()    
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Member sign up")
    print("2. See all members")
    print("3. Delete a member by ID")


if __name__ == "__main__":
    main()
