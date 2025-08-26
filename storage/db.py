import sqlite3

def init_db():
    conn = sqlite3.connect("marketresearch.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS research (
            id INTEGER PRIMARY KEY,
            company TEXT,
            use_cases TEXT,
            differentiators TEXT,
            market_strategy TEXT,
            pricing TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_data(data):
    conn = sqlite3.connect("marketresearch.db")
    c = conn.cursor()
    c.execute("""
        INSERT INTO research (company, use_cases, differentiators, market_strategy, pricing)
        VALUES (?, ?, ?, ?, ?)
    """, (data["company"], str(data["use_cases"]), str(data["differentiators"]), data["market_strategy"], data["pricing"]))
    conn.commit()
    conn.close()

def fetch_all():
    conn = sqlite3.connect("marketresearch.db")
    c = conn.cursor()
    c.execute("SELECT * FROM research")
    rows = c.fetchall()
    conn.close()
    return rows