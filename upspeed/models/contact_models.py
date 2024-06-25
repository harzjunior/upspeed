# models/contact.py

from upspeed.utils.db_config import get_db
import time

def create_contact(name, email, message):
    with get_db() as conn:
        cursor = conn.cursor()
        sql = "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, email, message))
        conn.commit()

def get_contacts():
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contacts")
        return cursor.fetchall()

# We can define more functions as needed, like delete_contact, update_contact, etc.
