#lib/cli.py

from helpers import (
    exit_program,
    member_sign_up,
    delete_member,
    gym_sign_up,
    get_all_gyms,
    delete_gym,
    find_member_by_first_name,
    find_gym_by_name
)
from models.member import Member
from models.gym import Gym
    
def details_members_menu(member, gym):

    while True:
        print("\nMember Details:")
        print(f"First name: {member.first_name}")
        print(f"Last name: {member.last_name}")
        print(f"Age: {member.age}")
        print(f"Gender: {member.gender}")
        print(f"Membership: {member.membership_type}\n")
        
        print("\nMember Details Menu:")
        print("B. Go back to the previous menu")
        print("D. Delete this member")
        print("E. Exit the program")
        choice = input("> ").upper()
        if choice == "E":
            exit_program()
        elif choice == "B":
            members_menu(gym)
        elif choice == "D":
            delete_member(member)
            members_menu(gym)
        else:
            print("Invalid choice. Please try again.")


def members_menu(gym):
    while True:
        print("\nMembers Menu:")
        members = gym.members()
        if members:
            print("Please select a member to see their details.")
            for index, member in enumerate(members, start=1):
                print(f"{index}. {member.first_name} {member.last_name}")
        else:
            print("No members in this gym.")

        print("\nB. Go back to the previous menu")
        print("A. Add a member in this gym")
        print("F. Find a member by first name")
        print("D. Delete this gym")
        print("E. Exit the program")
        choice = input("> ").upper()
        try:
            member_number = int(choice)
            if 1 <= member_number <= len(members):
                details_members_menu(members[member_number - 1], gym)
            else:
                print("Invalid member number. Please try again.")
        except ValueError:
            if choice == "E":
                exit_program()
            elif choice == "B":
                gyms_menu()
            elif choice == "D":
                result = delete_gym(gym.id)
                if result == "gyms_menu":
                    gyms_menu()
            elif choice == "A":
                result = member_sign_up(gym.id)
                if result == "members_menu":
                    members_menu(gym)
            elif choice == "F":
                member = find_member_by_first_name()
                if member:
                    details_members_menu(member, gym)
                else:
                    members_menu(gym)
            else:
                print("Invalid choice. Enter a number or menu option.")

def gyms_menu():
    while True:
        gyms = get_all_gyms()
        print("\nGyms Menu:")
        print("Please select a gym number to see its members.\n")
        print("B. Go back to the previous menu")
        print("A. Add a gym")
        print("F. Find a gym by name")
        print("E. Exit the program")
        choice = input("> ").upper()
        try:
            gym_number = int(choice)
            if 1 <= gym_number <= len(gyms):
                return members_menu(gyms[gym_number - 1])
            else:
                print("Invalid gym number. Please try again.")
        except ValueError:
            if choice == "E":
                exit_program()
            elif choice == "B":
                main()
            elif choice == "A":
                result = gym_sign_up()
                if result == "gyms_menu":
                    gyms_menu()
            elif choice == "F":
                gym = find_gym_by_name()
                if gym:
                    members_menu(gym)  # Proceed to the members menu if a gym is found
                else:
                    gyms_menu()  # Go back to gyms menu if gym not found
            else:
                print("Invalid choice. Enter a number or menu option.")

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
    print("E. Exit the program\n")

if __name__ == "__main__":
    main()

