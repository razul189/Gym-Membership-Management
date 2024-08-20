from models.__init__ import CONN, CURSOR
from models.member import Member  

class Gym:
    all = {}

    def __init__(self, name=None, location=None, opening_hours=None, closing_hours=None, gym_id=None):
        self.id = gym_id
        self.name = name
        self.location = location
        self.opening_hours = opening_hours
        self.closing_hours = closing_hours

    def __repr__(self):
        return (
            f"<Gym {self.id}: {self.name}, Location: {self.location}, "
            f"Opening Hours: {self.opening_hours}, Closing Hours: {self.closing_hours}>"
        )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or value.isdigit():
            raise ValueError("Invalid gym name.")
        self._name = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if not value or value.isdigit():
            raise ValueError("Invalid gym location.")
        self._location = value

    @property
    def opening_hours(self):
        return self._opening_hours

    @opening_hours.setter
    def opening_hours(self, value):
        from helpers import is_valid_time_format
        if not is_valid_time_format(value):
            raise ValueError("Invalid time format.")
        self._opening_hours = value

    @property
    def closing_hours(self):
        return self._closing_hours

    @closing_hours.setter
    def closing_hours(self, value):
        from helpers import is_valid_time_format
        if not is_valid_time_format(value):
            raise ValueError("Invalid time format.")
        self._closing_hours = value

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Gym instances """
        sql = """
            CREATE TABLE IF NOT EXISTS gyms (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT,
            opening_hours TEXT,
            closing_hours TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Gym instances """
        sql = """
            DROP TABLE IF EXISTS gyms;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name, location, opening_hours, and closing_hours values of the current Gym object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO gyms (name, location, opening_hours, closing_hours)
                VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.location, self.opening_hours, self.closing_hours))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Gym instance."""
        sql = """
            UPDATE gyms
            SET name = ?, location = ?, opening_hours = ?, closing_hours = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.location, self.opening_hours, self.closing_hours, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Gym instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM gyms
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, name, location, opening_hours, closing_hours):
        """ Initialize a new Gym instance and save the object to the database """
        gym = cls(name, location, opening_hours, closing_hours)
        gym.save()
        return gym

    @classmethod
    def instance_from_db(cls, row):
        """Return a Gym object having the attribute values from the table row."""

        # Check the dictionary for existing instance using the row's primary key
        gym = cls.all.get(row[0])
        if gym:
            # ensure attributes match row values in case local instance was modified
            gym.name = row[1]
            gym.location = row[2]
            gym.opening_hours = row[3]
            gym.closing_hours = row[4]
        else:
            # not in dictionary, create new instance and add to dictionary
            gym = cls(row[1], row[2], row[3], row[4])
            gym.id = row[0]
            cls.all[gym.id] = gym
        return gym

    @classmethod
    def get_all(cls):
        """Return a list containing one Gym object per table row"""
        sql = """
            SELECT *
            FROM gyms
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Gym object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM gyms
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_attribute(cls, attribute, value):
        """Find a Gym by a specified attribute and value."""
        sql = f"SELECT * FROM gyms WHERE {attribute} = ?"
        row = CURSOR.execute(sql, (value,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def members(self):
        """Return a list of Member objects belonging to this gym"""
        return Member.find_members_by_gym(self.id)


    
    
    
