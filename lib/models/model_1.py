from models.__init__ import CONN, CURSOR


class Member:
    
    def __init__(self, first_name=None, last_name=None, age=None, gender=None, membership_type=None, gym_id=None):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
        self._gender = gender
        self._membership_type = membership_type
        self._gym_id = gym_id

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    # Getter and Setter for last_name
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    # Getter and Setter for age
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    # Getter and Setter for gender
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    # Getter and Setter for membership_type
    @property
    def membership_type(self):
        return self._membership_type

    @membership_type.setter
    def membership_type(self, value):
        self._membership_type = value

    # Getter and Setter for gym_id
    @property
    def gym_id(self):
        return self._gym_id

    @gym_id.setter
    def gym_id(self, value):
        self._gym_id = value


    def register_member(self):
        CURSOR.execute(
            "INSERT INTO members (first_name, last_name, age, gender, membership_type, gym_id) VALUES (?,?,?,?,?,?)",
            (
                self.first_name,
                self.last_name,
                self.age,
                self.gender,
                self.membership_type,
                self.gym_id
            ),
        )
        CONN.commit()
        return CURSOR.lastrowid

    def create_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            age INTEGER,
            gender TEXT,
            membership_type TEXT CHECK (membership_type IN ('basic', 'silver', 'gold')),
            gym_id INTEGER,
            FOREIGN KEY (gym_id) REFERENCES gyms (id)
        );
        """
        CURSOR.execute(create_table_query)
        CONN.commit()

    def find_member_by_id(self, member_id):
        find_by_id_query = "SELECT * FROM members WHERE id = ?"
        CURSOR.execute(find_by_id_query, (member_id,))
        return CURSOR.fetchone()
    
    def find_member_by_name(self, first_name, last_name):
        find_by_name_query = "SELECT * FROM members WHERE first_name = ? AND last_name = ?"
        CURSOR.execute(find_by_name_query, (first_name, last_name))
        return CURSOR.fetchone()
    
    def delete_member(self, member_id):
        delete_member_query = "DELETE FROM members WHERE id = ?"
        CURSOR.execute(delete_member_query, (member_id,))
        CONN.commit()

    def delete_member_by_name(self, first_name, last_name):
        delete_member_query = "DELETE FROM members WHERE first_name = ? AND last_name = ?"
        CURSOR.execute(delete_member_query, (first_name, last_name))
        CONN.commit()

    def get_all_members(self):
        get_all_query = "SELECT * FROM members"
        CURSOR.execute(get_all_query)
        return CURSOR.fetchall()
    
    
class Gym:
    def __init__(self, name, location, opening_hours, closing_hours):
        self._name = name
        self._location = location
        self._opening_hours = opening_hours
        self._closing_hours = closing_hours

    # Getter and Setter for name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # Getter and Setter for location
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    # Getter and Setter for opening_hours
    @property
    def opening_hours(self):
        return self._opening_hours

    @opening_hours.setter
    def opening_hours(self, value):
        self._opening_hours = value

    # Getter and Setter for closing_hours
    @property
    def closing_hours(self):
        return self._closing_hours

    @closing_hours.setter
    def closing_hours(self, value):
        self._closing_hours = value
    
    def create_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS gyms (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT,
            opening_hours TIME,
            closing_hours TIME
        );
        """
        CURSOR.execute(create_table_query)
        CONN.commit()

    def find_gym_by_id(self, gym_id):
        find_by_id_query = "SELECT * FROM gyms WHERE id = ?"
        CURSOR.execute(find_by_id_query, (gym_id,))
        return CURSOR.fetchone()

    def register_gym(self):
        CURSOR.execute(
            "INSERT INTO gyms (name, location, opening_hours, closing_hours) VALUES (?,?,?,?)",
            (self.name, self.location, self.opening_hours, self.closing_hours),
        )
        CONN.commit()
        return CURSOR.lastrowid
    
    def delete_gym(self, gym_id):
        delete_gym_query = "DELETE FROM gyms WHERE id = ?"
        CURSOR.execute(delete_gym_query, (gym_id,))
        CONN.commit()

    def delete_gym_by_name(self, name):
        delete_gym_query = "DELETE FROM gyms WHERE name = ?"
        CURSOR.execute(delete_gym_query, (name,))
        CONN.commit()

    def get_all_gyms(self):
        get_all_query = "SELECT * FROM gyms"
        CURSOR.execute(get_all_query)
        return CURSOR.fetchall()
    
    def find_gym_by_name(self, name):
        find_by_name_query = "SELECT * FROM gyms WHERE name = ?"
        CURSOR.execute(find_by_name_query, (name,))
        return CURSOR.fetchone()
    
    
    
