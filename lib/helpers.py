# lib/helpers.py
#CREATE TABLE members( id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER, gender TEXT, membership_type TEXT CHECK (membership_type IN ("basic", "silver", "gold")), FOREIGN KEY (gym_id) REFERENCES gyms (id));

#CREATE TABLE gyms (id INTEGER PRIMARY KEY, name TEXT, location TEXT, opening_hours TIME, closing_hours TIME);
from models.model_1 import Member 

def exit_program():
    print("Goodbye!")
    exit()

def member_sign_up():
    print("\nEnter your first name.")
    first_name = input("> ")
    if not first_name:
        print("First name is empty.")
    elif first_name.isdigit():
        print("First name is a number.")

    print("Enter your last name.")
    last_name = input("> ")
    if not last_name:
        print("First name is empty.")
    elif last_name.isdigit():
        print("First name is a number.")

    try:
        print("Enter your age.")
        age = int(input("> "))
        if age < 14:
            print("You must be older than 14 to join.")
            return False
    except ValueError:
        print("Your age must be a number.")
        return False

    print("Enter your gender or enter N if you do not wish to specify.")
    gender = input("> ")

    print("\nSelect your membership type:")
    print("Option 1: basic")
    print("Option 2: silver")
    print("Option 3: gold")

    try:
        membership_type = int(input("> "))
        if membership_type == 1:
            membership_type = "basic"
        elif membership_type == 2:
            membership_type = "silver"
        elif membership_type == 3:
            membership_type = "gold"
        else:
            print("You must enter a valid option.")
            return False
    except ValueError:
        print("Your option must be a number.")
        return False

    gym_id = 1

    new_member = Member(first_name, last_name, age, gender, membership_type, gym_id)
    try:
        id_new_member = new_member.register_member()
        print(f"Member registered successfully with ID: {id_new_member}.\n")
        return True
    except Exception as e:
        print(f"Failed to register member: {e}")
        return False

def find_member_by_id():
    try:
        member_id = int(input("Enter the ID of the member "))
        member_manager = Member()
        member = member_manager.find_member_by_id(member_id)
        if not member:
            print("Member with the provided ID does not exist.")
            return
        print(member)
    except ValueError:
        print("Invalid input. Please enter a valid member ID.")


def get_all_members():
    member_manager = Member()
    member = member_manager.get_all_members()
    for m in member:
        print("ID: ",m[0])
        print("First name: ",m[1])
        print("Last name: ",m[2])
        print("Age: ",m[3])
        print("Gender: ",m[4])
        print("Membership type: ",m[5])
        print("Gym: ",m[6],"\n")

def delete_member():
    try:
        member_id = int(input("Enter the ID of the member you want to delete: "))
        member_manager = Member()
        member = member_manager.find_member_by_id(member_id)
        if not member:
            print("Member with the provided ID does not exist.")
            return

        confirm = input(f"Are you sure you want to delete member '{member_id}'? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Deletion cancelled.")
            return

        member_manager.delete_member(member_id)
        print("Member deleted successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid member ID.")

def delete_member_by_name():
    try:
        first_name = input("Enter the first name of the member you want to delete: ")
        last_name = input("Enter the last name of the member you want to delete: ")
        member_manager = Member()
        member = member_manager.find_member_by_name(first_name, last_name)
        if not member:
            print(f"No member with the name '{first_name} {last_name}' found.")
            return

        confirm = input(f"Are you sure you want to delete member '{first_name} {last_name}'? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Deletion cancelled.")
            return

        member_manager.delete_member_by_name(first_name, last_name)
        print(f"Member '{first_name} {last_name}' deleted successfully.")
    except Exception as e:
        print("Error:", e)




        