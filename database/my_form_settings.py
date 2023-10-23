import sqlite3

def form_import(user_id, name, surename, country, city, language, description, photo):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute(f'INSERT INTO forms (user_id, name, surename, country, city, language, description, photo) VALUES '
                f'("{user_id}", "{name}", "{surename}", "{country}", "{city}", "{language}", "{description}", "{photo}")')
    conn.commit()
    cur.close()
    conn.close()

def form_update(user_id, name, surename, country, city, language, description, photo):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute(f'UPDATE forms SET (name, surename, country, city, language, description, photo) = '
                f'("{name}", "{surename}", "{country}", "{city}", "{language}", "{description}", "{photo}") '
                f'WHERE user_id == "{user_id}"').fetchall()
    conn.commit()
    cur.close()
    conn.close()

def get_my_form(user_id):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    user = cur.execute('SELECT "user_id", "name", "surename", "country", "city", "language", "description", "photo"'
                       'FROM forms WHERE user_id == "{key}"'.format(key=user_id)).fetchall()
    return user

def update_photo(user_id, photo):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute(f'UPDATE forms SET(photo) = ("{photo}") WHERE user_id == "{user_id}"').fetchall()
    conn.commit()
    cur.close()
    conn.close()

def update_description(user_id, description):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute(f'UPDATE forms SET(description) = ("{description}") WHERE user_id == "{user_id}"').fetchall()
    conn.commit()
    cur.close()
    conn.close()