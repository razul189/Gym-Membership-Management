from models.__init__ import CONN, CURSOR

class Member:
    all = {}

    def __init__(self, first_name=None, last_name=None, age=None, gender=None, membership_type=None, gym_id=None, member_id=None):
        self.id = member_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.membership_type = membership_type
        self.gym_id = gym_id

    def __repr__(self):
        return (
            f"<Member {self.id}: {self.first_name} {self.last_name}, Age: {self.age}, "
            f"Gender: {self.gender}, Membership: {self.membership_type}, Gym ID: {self.gym_id}>"
        )

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not value or not value.isalpha():
            raise ValueError("Invalid first name.")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not value or not value.isalpha():
            raise ValueError("Invalid last name.")
        self._last_name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 14:
            raise ValueError("Age must be a number and you must be older than 14 to join.")
        self._age = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        if not value or (value.lower() not in ['male', 'female', 'n']):
            raise ValueError("Invalid gender.")
        self._gender = value

    @property
    def membership_type(self):
        return self._membership_type

    @membership_type.setter
    def membership_type(self, value):
        if value not in ['basic', 'silver', 'gold']:
            raise ValueError("Invalid membership type.")
        self._membership_type = value

    @property
    def gym_id(self):
        return self._gym_id

    @gym_id.setter
    def gym_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Invalid gym ID.")
        self._gym_id = value

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Member instances """
        sql = """
            CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            age INTEGER,
            gender TEXT,
            membership_type TEXT CHECK (membership_type IN ('basic', 'silver', 'gold')),
            gym_id INTEGER,
            FOREIGN KEY (gym_id) REFERENCES gyms(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Member instances """
        sql = """
            DROP TABLE IF EXISTS members;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the first_name, last_name, age, gender, membership_type, and gym_id values of the current Member object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO members (first_name, last_name, age, gender, membership_type, gym_id)
                VALUES (?, ?, ?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.first_name, self.last_name, self.age, self.gender, self.membership_type, self.gym_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Member instance."""
        sql = """
            UPDATE members
            SET first_name = ?, last_name = ?, age = ?, gender = ?, membership_type = ?, gym_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.first_name, self.last_name, self.age, self.gender, self.membership_type, self.gym_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Member instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM members
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, first_name, last_name, age, gender, membership_type, gym_id):
        """ Initialize a new Member instance and save the object to the database """
        member = cls(first_name, last_name, age, gender, membership_type, gym_id)
        member.save()
        return member

    @classmethod
    def instance_from_db(cls, row):
        """Return a Member object having the attribute values from the table row."""

        # Check the dictionary for existing instance using the row's primary key
        member = cls.all.get(row[0])
        if member:
            # ensure attributes match row values in case local instance was modified
            member.first_name = row[1]
            member.last_name = row[2]
            member.age = row[3]
            member.gender = row[4]
            member.membership_type = row[5]
            member.gym_id = row[6]
        else:
            # not in dictionary, create new instance and add to dictionary
            member = cls(row[1], row[2], row[3], row[4], row[5], row[6])
            member.id = row[0]
            cls.all[member.id] = member
        return member

    @classmethod
    def get_all(cls):
        """Return a list containing one Member object per table row"""
        sql = """
            SELECT *
            FROM members
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Member object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM members
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_members_by_gym(cls, gym_id):
        """Return a list of Member objects belonging to a specific gym"""
        sql = """
            SELECT *
            FROM members
            WHERE gym_id = ?
        """

        rows = CURSOR.execute(sql, (gym_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_attribute(cls, attribute, value):
        """Find a Member by a specified attribute and value."""
        sql = f"SELECT * FROM members WHERE {attribute} = ?"
        row = CURSOR.execute(sql, (value,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    
    
  
