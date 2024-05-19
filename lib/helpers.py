# lib/helpers.py
#CREATE TABLE members( id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER, gender TEXT, membership_type TEXT CHECK (membership_type IN ("basic", "silver", "gold")), FOREIGN KEY (gym_id) REFERENCES gyms (id));

#CREATE TABLE gyms (id INTEGER PRIMARY KEY, name TEXT, location TEXT, opening_hours TIME, closing_hours TIME);
from models.model_1 import Member 

def member_sign_up():
       
    print("Enter your first name.")
    first_name = input("> ")
        
    print("Enter your last name.")
    last_name = input("> ")

    print("Enter your age.")
    age = int(input("> "))

    if not isinstance(age, int): 
        print ("Your age must be a number")
        return False 
    if age < 14:
        print ("You must be older than 14 to join")
        return False 
    
    print("Enter your gender or enter N if you do not wish to specify")
    gender = input("> ")

    print("Select your membership type \n option 1: basic \n option 2: silver \n option 3: gold")

    membership_type = int(input("> "))

    if not isinstance(membership_type, int): 
        print ("Your option must be a number")
        return False 
    if membership_type != 1 and membership_type != 2 and membership_type != 3:
        print ("You must enter a valid option")
        return False 
    if membership_type == 1:
        membership_type = "basic"
    if membership_type == 2:
        membership_type = "silver"
    if membership_type == 3:
        membership_type = "gold"
    
    gym = 1

    new_member = Member(first_name, last_name, age, gender, membership_type)
    new_member.register_member()
    return True
    
        
def exit_program():
    print("Goodbye!")
    exit()
