import sqlite3

def fetch_user_data(user_input: str):
    conn = sqlite3.connect("production.db")
    cursor = conn.cursor()

    # Fix the vulnerability by using parameterized query
    cursor.execute("SELECT * FROM users WHERE username = ?", (user_input,))
    user_data = cursor.fetchall()

    conn.close()
    return user_data