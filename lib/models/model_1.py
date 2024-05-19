from models.__init__ import CONN, CURSOR


class Member:
    def __init__(self, first_name, last_name, age, gender, membership_type):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.membership_type = membership_type

    def register_member(self):
    

        CURSOR.execute("INSERT INTO members (first_name, last_name, age, gender, membership_type) VALUES (?,?,?,?,?)", 
                       (self.first_name, self.last_name, self.age, self.gender, self.membership_type))
        
        CONN.commit()


