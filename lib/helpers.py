# lib/helpers.py

from models.member import Member
from models.gym import Gym

def exit_program():
    print("Goodbye!")
    exit()

def member_sign_up(gym_id):
    first_name = input("\nEnter your first name: ").strip()
    if not first_name or first_name.isdigit():
        print("Invalid first name.")
        return "members_menu"

    last_name = input("Enter your last name: ").strip()
    if not last_name or last_name.isdigit():
        print("Invalid last name.")
        return "members_menu"

    try:
        age = int(input("Enter your age: ").strip())
        if age < 14:
            print("You must be older than 14 to join.")
            return "members_menu"
    except ValueError:
        print("Age must be a number.")
        return "members_menu"

    gender = input("Enter your gender or enter N if you do not wish to specify: ").strip()

    print("\nSelect the number of your membership type:")
    print("1. Basic")
    print("2. Silver")
    print("3. Gold")
    membership_types = {1: "basic", 2: "silver", 3: "gold"}
    try:
        membership_choice = int(input("> ").strip())
        membership_type = membership_types.get(membership_choice)
        if not membership_type:
            print("Invalid membership type.")
            return "members_menu"
    except ValueError:
        print("Membership type must be a number.")
        return "members_menu"

    try:
        Member.create(first_name, last_name, age, gender, membership_type, gym_id)
        print(f"\nMember registered successfully.")
    except Exception as e:
        print(f"Failed to register member: {e}")

    
def delete_member(member):
    try:
        confirm = input(f"\nAre you sure you want to delete member '{member.first_name}'? (yes/no): ").strip().lower()
        if confirm != 'yes':
            print("Deletion cancelled.")
            return "members_menu"

        member.delete()
        print("Member deleted successfully.")
        return "members_menu"

    except Exception as e:
        print(f"An error occurred while trying to delete the member: {e}")
        return "members_menu"

def gym_sign_up():
    name = input("\nEnter the gym name: ").strip()
    if not name or name.isdigit():
        print("\nInvalid gym name.")
        return "gyms_menu"

    location = input("Enter the gym location: ").strip()
    if not location or location.isdigit():
        print("\nInvalid gym location.")
        return "gyms_menu"

    opening_hours = input("Enter the opening hours (HH:MM format): ").strip()
    closing_hours = input("Enter the closing hours (HH:MM format): ").strip()

    if not is_valid_time_format(opening_hours) or not is_valid_time_format(closing_hours):
        print("\nInvalid time format.")
        return "gyms_menu"

    try:
        Gym.create(name, location, opening_hours, closing_hours)
        print(f"\nGym registered successfully.")
    except Exception as e:
        print(f"Failed to register gym: {e}")

def get_all_gyms():
    gyms = Gym.get_all()
    if not gyms:
        print("No gyms found.")
        return []
    for index, gym in enumerate(gyms, start=1):
        print(f"{index}. Name: {gym.name}, Location: {gym.location}, Opening Hours: {gym.opening_hours}, Closing Hours: {gym.closing_hours}")
    return gyms

def delete_gym(gym_id):
    gym = Gym.find_by_id(gym_id)
    if not gym:
        print("Gym not found.")
        return "gyms_menu"

    confirm = input(f"\nAre you sure you want to delete gym '{gym.name}'? This will also delete all associated members. (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("Deletion cancelled.")
        return "gyms_menu"

    # Delete all associated members
    for member in gym.members():
        member.delete()

    # Delete the gym
    gym.delete()
    print(f"\nGym '{gym.name}' and all associated members deleted successfully.\n")
    return "gyms_menu"

def find_member_by_first_name():
    first_name = input("\nEnter the first name of the member: ").strip()
    member = Member.find_by_attribute('first_name', first_name)
    if member:
        print(f"\nFound member: {member.first_name} {member.last_name}\n")
        return member
    else:
        print("Member not found.")
        return None

def find_gym_by_name():
    gym_name = input("\nEnter the name of the gym: ").strip()
    gym = Gym.find_by_attribute('name', gym_name)
    if gym:
        print(f"\nFound gym: {gym.name}, Location: {gym.location}, Opening Hours: {gym.opening_hours}, Closing Hours: {gym.closing_hours}")
        return gym
    else:
        print("Gym not found.")
        return None
    
def is_valid_time_format(time_str):
    try:
        hour, minute = map(int, time_str.split(":"))
        return 0 <= hour < 24 and 0 <= minute < 60
    except ValueError:
        return False
    
