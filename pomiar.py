import sqlite3

class Pomiar:
    _table_name = "pomiary"

    def __init__(self, dziecko_id, data, wzrost, waga, miesiace_zycia):
        self.dziecko_id = dziecko_id
        self.data = data
        self.wzrost = wzrost
        self.waga = waga
        self.miesiace_zycia = miesiace_zycia

    def print_pomiar(self):
        print(f"Waga: {self.waga} kg")
        print(f"Wzrost: {self.wzrost} cm")
        print(f"Data: {self.data}")

    @classmethod
    def create_table(cls):
        conn = sqlite3.connect('children.db')
        cursor = conn.cursor()

        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {cls._table_name} (
                id INTEGER PRIMARY KEY,
                dziecko_id INTEGER,
                data TEXT NOT NULL,
                wzrost REAL NOT NULL,
                waga REAL NOT NULL,
                miesiace_zycia REAL NOT NULL,
                FOREIGN KEY (dziecko_id) REFERENCES dzieci(id)
            )
        ''')

        conn.commit()
        conn.close()

    def save_to_db(self):
        conn = sqlite3.connect('children.db')
        cursor = conn.cursor()

        cursor.execute(f'''
            INSERT INTO {self._table_name} (dziecko_id, data, wzrost, waga, miesiace_zycia)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.dziecko_id, self.data, self.wzrost, self.waga, self.miesiace_zycia))

        conn.commit()
        conn.close()

    @classmethod
    def get_all_for_dziecko(cls, dziecko_id):
        conn = sqlite3.connect('children.db')
        cursor = conn.cursor()

        cursor.execute(f'''
            SELECT * FROM {cls._table_name}
            WHERE dziecko_id = ?
        ''', (dziecko_id,))

        rows = cursor.fetchall()
        measurements_list = []

        for row in rows:
            measurement = cls(*row[1:])
            measurements_list.append(measurement)

        conn.close()

        return measurements_list