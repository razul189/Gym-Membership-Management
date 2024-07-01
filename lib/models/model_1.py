# this is my model_1.py file

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

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @property
    def membership_type(self):
        return self._membership_type

    @membership_type.setter
    def membership_type(self, value):
        self._membership_type = value

    @property
    def gym_id(self):
        return self._gym_id

    @gym_id.setter
    def gym_id(self, value):
        self._gym_id = value

    def save(self):
        CURSOR.execute("""
        INSERT INTO members (first_name, last_name, age, gender, membership_type, gym_id) 
        VALUES (?, ?, ?, ?, ?, ?)""",
        (self.first_name, self.last_name, self.age, self.gender, self.membership_type, self.gym_id))
        CONN.commit()
        self.id = CURSOR.lastrowid

    def delete(self):
        CURSOR.execute("DELETE FROM members WHERE id = ?", (self.id,))
        CONN.commit()

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM members")
        return CURSOR.fetchall()

    @classmethod
    def find_by_id(cls, member_id):
        CURSOR.execute("SELECT * FROM members WHERE id = ?", (member_id,))
        return CURSOR.fetchone()

    @classmethod
    def find_members_by_gym(cls, gym_id):
        CURSOR.execute("SELECT * FROM members WHERE gym_id = ?", (gym_id,))
        return CURSOR.fetchall()

    @classmethod
    def delete_by_id(cls, member_id):
        CURSOR.execute("DELETE FROM members WHERE id = ?", (member_id,))
        CONN.commit()

class Gym:
    def __init__(self, name=None, location=None, opening_hours=None, closing_hours=None):
        self._name = name
        self._location = location
        self._opening_hours = opening_hours
        self._closing_hours = closing_hours

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def opening_hours(self):
        return self._opening_hours

    @opening_hours.setter
    def opening_hours(self, value):
        self._opening_hours = value

    @property
    def closing_hours(self):
        return self._closing_hours

    @closing_hours.setter
    def closing_hours(self, value):
        self._closing_hours = value

    def save(self):
        CURSOR.execute("""
        INSERT INTO gyms (name, location, opening_hours, closing_hours) 
        VALUES (?, ?, ?, ?)""",
        (self.name, self.location, self.opening_hours, self.closing_hours))
        CONN.commit()
        self.id = CURSOR.lastrowid

    def delete(self):
        CURSOR.execute("DELETE FROM gyms WHERE id = ?", (self.id,))
        CONN.commit()

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM gyms")
        return CURSOR.fetchall()

    @classmethod
    def find_by_id(cls, gym_id):
        CURSOR.execute("SELECT * FROM gyms WHERE id = ?", (gym_id,))
        return CURSOR.fetchone()

    @classmethod
    def delete_by_id(cls, gym_id):
        CURSOR.execute("DELETE FROM gyms WHERE id = ?", (gym_id,))
        CONN.commit()

