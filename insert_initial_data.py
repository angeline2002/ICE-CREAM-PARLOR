import sqlite3

def insert_initial_data():
    conn = sqlite3.connect('icecream_parlor.db')
    cursor = conn.cursor()

    flavors = [
        ('Vanilla', 'All'),
        ('Chocolate', 'All'),
        ('Strawberry', 'Summer'),
        ('Pumpkin Spice', 'Fall')
    ]
    cursor.executemany('INSERT INTO flavors (name, season) VALUES (?, ?)', flavors)

    ingredients = [
        ('Milk', 100),
        ('Sugar', 50),
        ('Cocoa', 30)
    ]
    cursor.executemany('INSERT INTO ingredients (name, quantity) VALUES (?, ?)', ingredients)

    allergens = [
        ('Peanuts',),
        ('Gluten',),
        ('Lactose',)
    ]
    cursor.executemany('INSERT INTO allergens (name) VALUES (?)', allergens)

    flavor_allergens = [
        (1, 3),  # Vanilla - Lactose
        (2, 3),  # Chocolate - Lactose
        (3, 3),  # Strawberry - Lactose
        (4, 2)   # Pumpkin Spice - Gluten
    ]
    cursor.executemany('INSERT INTO flavor_allergens (flavor_id, allergen_id) VALUES (?, ?)', flavor_allergens)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_initial_data()
