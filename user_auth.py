import sqlite3
from hashlib import sha256

def hash_password(password):
    return sha256(password.encode()).hexdigest()

def register_user(username, password):
    conn = sqlite3.connect('backup_recovery.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                       (username, hash_password(password)))
        conn.commit()
    except sqlite3.IntegrityError:
        raise ValueError("Username already exists.")
    finally:
        conn.close()

def authenticate_user(username, password):
    conn = sqlite3.connect('backup_recovery.db')
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
    stored_password = cursor.fetchone()
    conn.close()
    if stored_password and stored_password[0] == hash_password(password):
        return True
    return False
