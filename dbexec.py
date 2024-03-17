import sqlite3


class DbExec():

    def __init__(self):
        self.db = sqlite3.connect('../server.db')
        self.cursor = self.db.cursor()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY , 
            name TEXT,
            hash TEXT
        )""")
        self.db.commit()
        # self.db.close()

    def add_data(self, name, hash):
        query = f"INSERT INTO notes (name,hash) VALUES ('{name}', '{hash}')"
        self.cursor.execute(query)
        self.db.commit()

    def close_connect(self):
        self.db.close()

    def show_duplicate(self):
        query = "SELECT id " \
                "FROM notes " \
                "GROUP BY hash HAVING COUNT(*)>1 " \
                "ORDER BY COUNT(*) desc"

        self.cursor.execute(query)
        duplicate = self.cursor.fetchall()
        print(duplicate)


# db = DbExec()
# db.create_table()
# db.add_data('1323', '00')
# db.show_duplicate()
