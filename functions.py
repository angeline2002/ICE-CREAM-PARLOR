import sqlite3

def add_to_cart(user_id, flavor_id):
    conn = sqlite3.connect('icecream_parlor.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO carts (user_id, flavor_id) VALUES (?, ?)', (user_id, flavor_id))
    conn.commit()
    conn.close()

def search_offerings(season=None):
    conn = sqlite3.connect('icecream_parlor.db')
    cursor = conn.cursor()
    if season:
        cursor.execute('''SELECT flavors.id, flavors.name, flavors.season, GROUP_CONCAT(DISTINCT allergens.name) AS allergens
                          FROM flavors
                          LEFT JOIN flavor_allergens ON flavors.id = flavor_allergens.flavor_id
                          LEFT JOIN allergens ON flavor_allergens.allergen_id = allergens.id
                          WHERE flavors.season = ?
                          GROUP BY flavors.id, flavors.name, flavors.season''', (season,))
    else:
        cursor.execute('''SELECT flavors.id, flavors.name, flavors.season, GROUP_CONCAT(DISTINCT allergens.name) AS allergens
                          FROM flavors
                          LEFT JOIN flavor_allergens ON flavors.id = flavor_allergens.flavor_id
                          LEFT JOIN allergens ON flavor_allergens.allergen_id = allergens.id
                          GROUP BY flavors.id, flavors.name, flavors.season''')
    results = cursor.fetchall()
    conn.close()
    return results

def add_allergen(name):
    conn = sqlite3.connect('icecream_parlor.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO allergens (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()

def view_cart(user_id):
    conn = sqlite3.connect('icecream_parlor.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT flavors.name FROM carts
                      JOIN flavors ON carts.flavor_id = flavors.id
                      WHERE carts.user_id = ?''', (user_id,))
    results = cursor.fetchall()
    conn.close()
    return results
