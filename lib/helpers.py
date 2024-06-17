# lib/helpers.py

from models.model_1 import Member, Gym 

def exit_program():
    print("Goodbye!")
    exit()

def member_sign_up(gym_id):
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

    new_member = Member(first_name, last_name, age, gender, membership_type, gym_id)
    try:
        id_new_member = new_member.register_member()
        print(f"Member registered successfully with ID: {id_new_member}.\n")
        return True
    except Exception as e:
        print(f"Failed to register member: {e}")
        return False

def find_member_by_id(member_number,gym_id):
    try:
        member_id = member_number
        member_manager = Member()
        member = member_manager.find_member_by_id(member_id)
        if not member:
            print("Member with the provided ID does not exist.\n\n\n\n")
            return False
        if member[6] != gym_id:
            print("Not a member of this gym\n\n\n\n")
            return False
        print("Member:")
        print(f"First name: {member[1]}")
        print(f"Last name: {member[2]}")
        print(f"Age: {member[3]}")
        print(f"Gender: {member[4]}")
        print(f"Membership: {member[5]}")
        print("\n\n")
        return True
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

def delete_member(member_number):
    try:
        member_id = member_number
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

def gym_sign_up():
    print("Enter the gym name.")
    name = input("> ")
    if not name:
        print("Gym name is empty.")
        return False
    elif name.isdigit():
        print("Gym name cannot be a number.")
        return False

    print("Enter the gym location.")
    location = input("> ")
    if not location:
        print("Gym location is empty.")
        return False
    elif location.isdigit():
        print("Gym location cannot be a number.")
        return False

    print("Enter the opening hours (HH:MM format).")
    opening_hours = input("> ")
    if not opening_hours:
        print("Opening hours is empty.")
        return False

    print("Enter the closing hours (HH:MM format).")
    closing_hours = input("> ")
    if not closing_hours:
        print("Closing hours is empty.")
        return False

    # Validate time format (HH:MM)
    def is_valid_time_format(time_str):
        try:
            hour, minute = map(int, time_str.split(":"))
            return 0 <= hour < 24 and 0 <= minute < 60
        except ValueError:
            return False

    if not is_valid_time_format(opening_hours):
        print("Opening hours is not in a valid HH:MM format.")
        return False

    if not is_valid_time_format(closing_hours):
        print("Closing hours is not in a valid HH:MM format.")
        return False

    new_gym = Gym(name, location, opening_hours, closing_hours)
    try:
        id_new_gym = new_gym.register_gym()
        print(f"Gym registered successfully with ID: {id_new_gym}.")
        return True
    except Exception as e:
        print(f"Failed to register gym: {e}")
        return False
    
def get_all_gyms():
    gym_manager = Gym("", "", "", "")
    gyms = gym_manager.get_all_gyms()
    for g in gyms:
        print(str(g[0])+ ". ", g[1],"\n")

def get_gym_by_id(gym_number):
    try:
        gym_id = gym_number
        gym_manager = Gym("", "", "", "")
        member_manager = Member()
        gym = gym_manager.find_gym_by_id(gym_id)
        if not gym:
            print("Gym with the provided ID does not exist.")
            return
        print(f"ID: {gym[0]}")
        print(f"Name: {gym[1]}")
        print(f"Location: {gym[2]}")
        print(f"Opening Hours: {gym[3]}")
        print(f"Closing Hours: {gym[4]}")
        print()
        gym_members = member_manager.find_members_by_gym(gym_id)
        if not gym_members:
            print("No gym members\n\n\n\n")
            return
        print("Gym's members")
        for member in gym_members:
            print(f"{member[0]}. {member[1]} {member[2]}")
    except ValueError:
        print("Invalid input. Please enter a valid gym ID.")

def delete_gym_by_id(gym_number):
    try:
        gym_id = gym_number
        gym_manager = Gym("", "", "", "")
        gym = gym_manager.find_gym_by_id(gym_id)
        if not gym:
            print(f"No gym with ID {gym_id} found.")
            return

        confirm = input(f"Are you sure you want to delete gym with ID {gym_id}? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Deletion cancelled.")
            return

        gym_manager.delete_gym(gym_id)
        print(f"Gym with ID {gym_id} deleted successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid gym ID.")
    except Exception as e:
        print("Error:", e)

