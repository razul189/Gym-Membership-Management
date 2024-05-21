# lib/cli.py

from helpers import (
    exit_program,
    member_sign_up,
    find_member_by_id,
    get_all_members,
    delete_member,
    delete_member_by_name
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
            find_member_by_id()
        elif choice == "3":
            get_all_members()
        elif choice == "4":
             delete_member()
        elif choice == "5":
            delete_member_by_name()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Member sign up")
    print("2. Find a member by ID")
    print("3. See all members")
    print("4. Delete a member by ID")
    print("5. Delete a member by name")
    


if __name__ == "__main__":
    main()
