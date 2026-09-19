import sqlite3


class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_users_table()

    def create_users_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NULL UNIQUE,
                name TEXT NULL,
                step TEXT NULL,
                partner_id TEXT NULL
            )
        """)
        self.connection.commit()

    def add_user(self, user_id, name, step=None, partner_id=None):
        self.cursor.execute(
            """
            INSERT INTO users (user_id, name, step, partner_id)
            VALUES (?, ?, ?, ?)
        """,
            (user_id, name, step, partner_id),
        )
        self.connection.commit()

    def get_user(self, user_id):
        self.cursor.execute(
            """
            SELECT * FROM users WHERE user_id = ?
        """,
            (user_id,),
        )
        return self.cursor.fetchone()

    def setPartner(self, user_id, partner_id):
        self.cursor.execute(
            """
            UPDATE users SET partner_id = ? WHERE user_id = ?
        """,
            (partner_id, user_id),
        )
        self.connection.commit()

    def setStep(self, user_id, step):
        self.cursor.execute(
            """
            UPDATE users SET step = ? WHERE user_id = ?
        """,
            (step, user_id),
        )
        self.connection.commit()

    def getStep(self, user_id):
        self.cursor.execute(
            """
        SELECT step FROM users WHERE user_id = ?
        """,
            (user_id,),
        )

        result = self.cursor.fetchone()
        return result[0]

    def getUserWaiting(self, user_id):
       self.cursor.execute(
        """
        SELECT user_id FROM users
        WHERE step = 'waiting'
        AND user_id != ?
        ORDER BY RANDOM()
        LIMIT 1
        """,
        (user_id,),
    )
       return self.cursor.fetchone()

        
db = Database("anonymousChat.db")
