import sqlite3
from datetime import datetime
import os

DB_DIR = "database"
DB_PATH = os.path.join(DB_DIR, "history.db")

def init_db():
    os.makedirs(DB_DIR, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_chat(question, answer):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO chat_history (question, answer, timestamp)
        VALUES (?, ?, ?)
    """, (question, answer, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    conn.commit()
    conn.close()


def get_all_chats():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT question, answer, timestamp
        FROM chat_history
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows


def clear_chats():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM chat_history")
    conn.commit()
    conn.close()

