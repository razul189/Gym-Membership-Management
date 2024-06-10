# lib/cli.py

from helpers import (
    exit_program,
    member_sign_up,
    find_member_by_id,
    get_all_members,
    delete_member,
    delete_member_by_name,
    gym_sign_up,
    get_all_gyms,
    get_gym_by_id,
    delete_gym_by_id
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
        elif choice == "6":
            gym_sign_up()
        elif choice == "7":
            get_all_gyms()
        elif choice == "8":
            get_gym_by_id()
        elif choice == "9":
            delete_gym_by_id()
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
    print("6. Register a gym")
    print("7. Display all gyms")
    print("8. Display gym by ID")
    print("9. Delete a gym by ID")

    

if __name__ == "__main__":
    main()
