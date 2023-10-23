import sqlite3

def liked_form_id(user_id):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    random_like = cur.execute(f'SELECT "id", "sender" FROM likes WHERE "recipient" == "{user_id}" LIMIT 1').fetchone()
    if random_like == None:
        return False
    likers_form = cur.execute(f'SELECT "user_id", "name", "surename", "country", "city", "language", "description", "photo"'
                       f'FROM forms WHERE user_id == "{random_like[1]}"').fetchone()
    cur.execute(f'DELETE FROM likes WHERE "id" == {random_like[0]}')
    conn.commit()
    cur.close()
    conn.close()
    return likers_form