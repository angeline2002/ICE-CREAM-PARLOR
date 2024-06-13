import sqlite3

def setup_database():
    conn = sqlite3.connect('icecream_parlor.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS flavors (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        season TEXT
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS ingredients (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        quantity INTEGER NOT NULL
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS allergens (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS flavor_allergens (
                        id INTEGER PRIMARY KEY,
                        flavor_id INTEGER,
                        allergen_id INTEGER,
                        FOREIGN KEY (flavor_id) REFERENCES flavors(id),
                        FOREIGN KEY (allergen_id) REFERENCES allergens(id)
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS user_allergens (
                        id INTEGER PRIMARY KEY,
                        user_id INTEGER,
                        allergen_id INTEGER,
                        FOREIGN KEY (user_id) REFERENCES users(id),
                        FOREIGN KEY (allergen_id) REFERENCES allergens(id)
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS carts (
                        id INTEGER PRIMARY KEY,
                        user_id INTEGER,
                        flavor_id INTEGER,
                        FOREIGN KEY (user_id) REFERENCES users(id),
                        FOREIGN KEY (flavor_id) REFERENCES flavors(id)
                    )''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
