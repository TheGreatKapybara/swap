import sqlite3

def check_my_form(user_id):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    user = cur.execute('SELECT 1 FROM forms WHERE user_id == "{key}"'.format(key=user_id)).fetchone()
    if not user:
        return False
    else:
        return True