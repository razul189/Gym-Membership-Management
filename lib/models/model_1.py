from models.__init__ import CONN, CURSOR


class Member:
    def __init__(self, first_name=None, last_name=None, age=None, gender=None, membership_type=None, gym_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.membership_type = membership_type
        self.gym_id = gym_id


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


