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

def details_members_menu(member_number,gym_id):
    if not find_member_by_id(member_number,gym_id):
        return
    print("B. Go back to the previous menu")
    print("D. Delete this member")
    print("E. Exit the program")
    choice = input("> ")
    if choice.upper() in ( "B", "U", "D", "E"):
        if choice.upper() == "E":
            exit_program()
        elif choice.upper() == "B":
            pass
        elif choice.upper() == "D":
            delete_member(member_number)
            members_menu
        else:
            print("Invalid choice. Please try again.")
            gyms_menu()

def members_menu(gym_number):
    get_gym_by_id(gym_number)
    print("Please select a member to see their details.")
    print("B. Go back to the previous menu")
    print("A. Add a member in this gym")
    print("D. Delete this gym")
    print("E. Exit the program")
    choice = input("> ")
    try:
        member_number = int(choice)
        details_members_menu(member_number,gym_number)
        members_menu(gym_number)
    except ValueError:
        if choice.upper() in ("E", "B",  "A", "D"):
            if choice.upper() == "E":
                exit_program()
            elif choice.upper() == "B":
                return
            elif choice.upper() == "D":
                delete_gym_by_id(gym_number)
            elif choice.upper() == "A":
                member_sign_up(gym_number)
                members_menu(gym_number)
            else:
                print("Invalid choice. Please try again.")
                members_menu(gym_number)
        else:
            print("Invalid choice. Enter a number or menu option.")
            members_menu(gym_number)

def gyms_menu():
  get_all_gyms()
  print("Please select a gym to see its details.")
  print("B. Go back to the previous menu")
  print("A. Add a gym")
  print("E. Exit the program")

  choice = input("> ")

  try:
    gym_number = int(choice)
    members_menu(gym_number)
    gyms_menu()
  except ValueError:
    if choice.upper() in ("E", "B", "A"):
      if choice.upper() == "E":
        exit_program()
      elif choice.upper() == "B":
        pass
      elif choice.upper() == "A":
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
        choice = input("> ")
        if choice == "e" or choice== "E":
            exit_program()
        elif choice == "G" or choice == "g":
            gyms_menu()
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
    print("G. Gyms")
    print("E. Exit the program")


if __name__ == "__main__":
    main()
