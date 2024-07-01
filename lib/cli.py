# lib/cli.py

from helpers import (
    exit_program,
    member_sign_up,
    find_member_by_id,
    delete_member,
    gym_sign_up,
    get_all_gyms,
    get_gym_by_id,
    delete_gym_by_id
)

def details_members_menu(member_number, gym_id):
    if not find_member_by_id(member_number, gym_id):
        return
    print("\nMember Details Menu:")
    print("B. Go back to the previous menu")
    print("D. Delete this member")
    print("E. Exit the program")
    choice = input("> ").upper()
    if choice == "E":
        exit_program()
    elif choice == "B":
        pass
    elif choice == "D":
        delete_member(member_number)
        members_menu(gym_id)
    else:
        print("Invalid choice. Please try again.")
        details_members_menu(member_number, gym_id)

def members_menu(gym_number):
    members_keys = get_gym_by_id(gym_number)
    print("\nMembers Menu:")
    print("Please select a member to see their details.")
    print("B. Go back to the previous menu")
    print("A. Add a member in this gym")
    print("D. Delete this gym")
    print("E. Exit the program")
    choice = input("> ").upper()
    try:
        member_number = int(choice)
        member_number = members_keys.get(member_number, 0)
        details_members_menu(member_number, gym_number)
        members_menu(gym_number)
    except ValueError:
        if choice in ("E", "B", "A", "D"):
            if choice == "E":
                exit_program()
            elif choice == "B":
                return
            elif choice == "D":
                delete_gym_by_id(gym_number)
            elif choice == "A":
                member_sign_up(gym_number)
                members_menu(gym_number)
            else:
                print("Invalid choice. Please try again.")
                members_menu(gym_number)
        else:
            print("Invalid choice. Enter a number or menu option.")
            members_menu(gym_number)

def gyms_menu():
    gym_keys = get_all_gyms()
    print("\nGyms Menu:")
    print("Please select a gym number to see its details.")
    print("B. Go back to the previous menu")
    print("A. Add a gym")
    print("E. Exit the program")
    choice = input("> ").upper()
    try:
        gym_number = int(choice)
        gym_number = gym_keys.get(gym_number, 0)
        members_menu(gym_number)
        gyms_menu()
    except ValueError:
        if choice in ("E", "B", "A"):
            if choice == "E":
                exit_program()
            elif choice == "B":
                pass
            elif choice == "A":
                gym_sign_up()
                gyms_menu()
            else:
                print("Invalid choice. Please try again.")
                gyms_menu()
        else:
            print("Invalid choice. Enter a number or menu option.")
            gyms_menu()

def main():
    while True:
        menu()
        choice = input("> ").upper()
        if choice == "E":
            exit_program()
        elif choice == "G":
            gyms_menu()
        else:
            print("Invalid choice")

def menu():
    print("\nMain Menu:")
    print("G. Gyms")
    print("E. Exit the program")

if __name__ == "__main__":
    main()

