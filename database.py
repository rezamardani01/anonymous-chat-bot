import sqlite3


class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_users_table()
        self.create_chat_requests_table()

    def create_users_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT UNIQUE,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            bio TEXT,
            profile_like INTEGER DEFAULT 0,
            step TEXT
        )
    """)

    self.connection.commit()

    def create_chat_requests_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            gender TEXT NULL,
            min_age INTEGER NULL,
            max_age INTEGER NULL,
            status TEXT DEFAULT 'waiting',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    self.connection.commit()

    def add_user(self, user_id, name, age, gender, step=None, partner_id=None):
        self.cursor.execute(
            """
            INSERT INTO users (user_id, name, age, gender, step, partner_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """,
            (user_id, name, step, partner_id),
        )
        self.connection.commit()

    def get_user(self, user_id):
        self.cursor.execute(
            """
            SELELCT FROM users WHERE user_id = ?
            """,
            (user_id,),
        )

        return self.cursor.fetchone()

    def set_step(self, user_id, step):
        self.cursor.execute(
            """
            UPDATE users SET step = ? WHERE user_id = ?
            """,
            (step, user_id),
        )
        self.connection.commit()


db = Database("anonymousChat.db")
