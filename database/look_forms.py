import sqlite3
import random

def random_forms():
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    length = cur.execute('SELECT COUNT (*) FROM forms').fetchone()
    random_id = random.randint(1,length[0])
    random_form = cur.execute('SELECT "user_id", "name", "surename", "country", "city", "language", "description", "photo"'
                       'FROM forms WHERE id == "{key}"'.format(key=random_id)).fetchone()
    return random_form

def safe_like(sender, recipient):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute(f'INSERT INTO likes (sender, recipient) VALUES ("{sender}", "{recipient}")')
    conn.commit()
    cur.close()
    conn.close()

def like_counter(user_id):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    number_of_likes = cur.execute(f'SELECT COUNT (*) FROM likes WHERE "recipient" == "{user_id}"').fetchall()
    return number_of_likes[0][0]