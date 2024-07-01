# lib/helpers.py

from models.model_1 import Member, Gym 

def exit_program():
    print("Goodbye!")
    exit()

def member_sign_up(gym_id):
    first_name = input("Enter your first name: ").strip()
    if not first_name or first_name.isdigit():
        print("Invalid first name.")
        return False

    last_name = input("Enter your last name: ").strip()
    if not last_name or last_name.isdigit():
        print("Invalid last name.")
        return False

    try:
        age = int(input("Enter your age: ").strip())
        if age < 14:
            print("You must be older than 14 to join.")
            return False
    except ValueError:
        print("Age must be a number.")
        return False

    gender = input("Enter your gender or enter N if you do not wish to specify: ").strip()

    print("\nSelect your membership type:")
    print("1. Basic")
    print("2. Silver")
    print("3. Gold")
    membership_types = {1: "basic", 2: "silver", 3: "gold"}
    try:
        membership_choice = int(input("> ").strip())
        membership_type = membership_types.get(membership_choice)
        if not membership_type:
            print("Invalid membership type.")
            return False
    except ValueError:
        print("Membership type must be a number.")
        return False

    new_member = Member(first_name, last_name, age, gender, membership_type, gym_id)
    try:
        new_member.save()
        print(f"Member registered successfully\n")
        return True
    except Exception as e:
        print(f"Failed to register member: {e}")
        return False

def find_member_by_id(member_number, gym_id):
    try:
        member = Member.find_by_id(member_number)
        if not member:
            print("Member with the provided ID does not exist.\n")
            return False
        if member[6] != gym_id:
            print("Not a member of this gym.\n")
            return False
        print("Member Details:")
        print(f"First name: {member[1]}")
        print(f"Last name: {member[2]}")
        print(f"Age: {member[3]}")
        print(f"Gender: {member[4]}")
        print(f"Membership: {member[5]}\n")
        return True
    except ValueError:
        print("Invalid member ID.")
        return False

def delete_member(member_number):
    try:
        member = Member.find_by_id(member_number)
        if not member:
            print("Member with the provided ID does not exist.")
            return

        confirm = input(f"Are you sure you want to delete member '{member[1]}'? (yes/no): ").strip().lower()
        if confirm != 'yes':
            print("Deletion cancelled.")
            return

        Member.delete_by_id(member_number)
        print("Member deleted successfully.")
    except ValueError:
        print("Invalid member ID.")

def gym_sign_up():
    name = input("Enter the gym name: ").strip()
    if not name or name.isdigit():
        print("Invalid gym name.")
        return False

    location = input("Enter the gym location: ").strip()
    if not location or location.isdigit():
        print("Invalid gym location.")
        return False

    opening_hours = input("Enter the opening hours (HH:MM format): ").strip()
    closing_hours = input("Enter the closing hours (HH:MM format): ").strip()

    if not is_valid_time_format(opening_hours) or not is_valid_time_format(closing_hours):
        print("Invalid time format.")
        return False

    new_gym = Gym(name, location, opening_hours, closing_hours)
    try:
        new_gym.save()
        print(f"Gym registered successfully with ID: {new_gym.id}.")
        return True
    except Exception as e:
        print(f"Failed to register gym: {e}")
        return False

def is_valid_time_format(time_str):
    try:
        hour, minute = map(int, time_str.split(":"))
        return 0 <= hour < 24 and 0 <= minute < 60
    except ValueError:
        return False

def get_all_gyms():
    gym_keys = {}
    gyms = Gym.get_all()
    if not gyms:
        print("No gyms found.")
    counter = 1 
    for gym in gyms:
        gym_keys[counter] = gym[0] 
        print (f"{counter}, Name: {gym[1]}, Location: {gym[2]}")
        counter = counter + 1
    return gym_keys

def get_gym_by_id(gym_number):
    try:
        
        gym = Gym.find_by_id(gym_number)
        if not gym:
            print("Selected gym does not exist.")
            return
        print(f"Name: {gym[1]}")
        print(f"Location: {gym[2]}")
        print(f"Opening Hours: {gym[3]}")
        print(f"Closing Hours: {gym[4]}")
        print()
        members = Member.find_members_by_gym(gym_number)
        if not members:
            print("No members in this gym.")
            return
        print("Gym Members:")
        members_keys = {}
        counter = 1
        for member in members:
            members_keys[counter] = member[0]
            print(f"{counter}. {member[1]} {member[2]}")
            counter = counter + 1
        return members_keys
    except ValueError:
        print("Invalid gym ID.")

def delete_gym_by_id(gym_id):
    try:
        gym = Gym.find_by_id(gym_id)
        if not gym:
            print(f"No gym with ID {gym_id} found.")
            return

        confirm = input(f"Are you sure you want to delete gym with ID {gym_id}? (yes/no): ").strip().lower()
        if confirm != 'yes':
            print("Deletion cancelled.")
            return

        Gym.delete_by_id(gym_id)
        print(f"Gym with ID {gym_id} deleted successfully.")
    except ValueError:
        print("Invalid gym ID.")
    except Exception as e:
        print(f"Error: {e}")
