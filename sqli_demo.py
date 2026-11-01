import sqlite3

def fetch_user_data(user_input: str):
    conn = sqlite3.connect("production.db")
    cursor = conn.cursor()
    
    # Vulnerable SQL Injection: Direct string concatenation inside query
    query = "SELECT * FROM users WHERE username = '" + user_input + "'"
    
    cursor.execute(query)
    return cursor.fetchall()
