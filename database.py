import sqlite3

def initialize_database():
    conn = sqlite3.connect('backup_recovery.db')
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS backups (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      filename TEXT,
                      destination TEXT,
                      source TEXT,
                      compression TEXT,
                      encryption TEXT,
                      schedule TEXT,
                      timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT UNIQUE,
                      password TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS logs (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      message TEXT,
                      timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')

    conn.commit()
    conn.close()

initialize_database()
