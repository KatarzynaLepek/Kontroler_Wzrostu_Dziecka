import sqlite3

class Dziecko:
    _table_name = "dzieci"
    _pomiary_table_name = "pomiary"

    def __init__(self, id, imie, plec, data_urodzenia):
        self.id = id
        self.imie = imie
        self.plec = plec
        self.data_urodzenia = data_urodzenia

    @classmethod
    def create_table(cls):
        conn = sqlite3.connect('children.db')
        cursor = conn.cursor()

        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {cls._table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                imie TEXT NOT NULL,
                plec TEXT NOT NULL,
                data_urodzenia TEXT NOT NULL
            )
        ''')

        conn.commit()
        conn.close()

    def save_to_db(self):
        conn = sqlite3.connect('children.db')
        cursor = conn.cursor()

        cursor.execute(f'''
            INSERT INTO {self._table_name} (imie, plec, data_urodzenia)
            VALUES (?, ?, ?)
        ''', (self.imie, self.plec, self.data_urodzenia))

        conn.commit()
        conn.close()

    @classmethod
    def get_all_from_db(cls):
        conn = sqlite3.connect('children.db')
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {cls._table_name}")
        rows = cursor.fetchall()

        children_list = []
        for row in rows:
            child = cls(*row[:])
            children_list.append(child)

        conn.close()

        return children_list

    @classmethod
    def get_by_id(cls, dziecko_id):
        conn = sqlite3.connect('children.db')
        cursor = conn.cursor()

        cursor.execute(f'''
            SELECT * FROM {cls._table_name}
            WHERE id = ?
        ''', (dziecko_id,))

        result = cursor.fetchone()
        conn.close()

        if result:
            dziecko = cls(*result[:])
            return dziecko
        else:
            return None

    @classmethod
    def exists_with_id(cls, dziecko_id):
        conn = sqlite3.connect('children.db')
        cursor = conn.cursor()

        cursor.execute(f'''
            SELECT COUNT(*) FROM {cls._table_name}
            WHERE id = ?
        ''', (dziecko_id,))

        count = cursor.fetchone()[0]
        conn.close()

        return count > 0

    def print_dziecko(self):
        print(f"ID: {self.id}")
        print(f"Imię: {self.imie}")
        print(f"Płeć: {self.plec}")
        print(f"Data Urodzenia: {self.data_urodzenia}")

