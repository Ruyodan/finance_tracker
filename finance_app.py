# =========================
# IMPORTS
# =========================
# Always import Flask (for web app) and sqlite3 (for database)
from flask import Flask, render_template, request
import sqlite3

# =========================
# CREATE FLASK APP
# =========================
# This line is always the same in every Flask project
app = Flask(__name__)

# =========================
# DATABASE SETUP
# =========================
def init_db():
    # Connect to SQLite file (creates it if missing)
    # Path "database/finance.db" → customizable (depends on your folder name)
    conn = sqlite3.connect("database/finance.db")
    cursor = conn.cursor()

    # Create the transactions table if it doesn't exist
    # Table name "transactions" → customizable
    # Column names (amount, type, description, timestamp) → customizable
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,   -- Always base: unique ID
            amount REAL NOT NULL,                   -- Customizable: field name/type
            type TEXT NOT NULL,                     -- Customizable: field name/type
            description TEXT,                       -- Customizable: optional field
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP -- Always base: useful for time
        )
    """)

    # Always commit changes and close connection
    conn.commit()
    conn.close()

# Call this once when app starts → always base
init_db()

# =========================
# ROUTE: Homepage
# =========================
@app.route("/")   # Always base: defines route
def home():
    # Always base: render_template links HTML file in /templates
    return render_template("home.html")

# =========================
# ROUTE: Handle Form Submission
# =========================
@app.route("/add", methods=["POST"])   # Always base: POST route for forms
def add_transaction():
    # Always base: request.form[...] to get values from HTML form
    amount = request.form["amount"]          # Customizable: field name
    t_type = request.form["type"]            # Customizable: field name
    description = request.form["description"]# Customizable: field name

    # Connect to database → always base
    conn = sqlite3.connect("database/finance.db")
    cursor = conn.cursor()

    # Insert new transaction → customizable table/fields
    cursor.execute("""
        INSERT INTO transactions (amount, type, description)
        VALUES (?, ?, ?)
    """, (amount, t_type, description))

    # Always commit and close
    conn.commit()
    conn.close()

    # Return confirmation → customizable (later we’ll redirect to summary page)
    return f"Saved {t_type}: {amount} ({description})"

# =========================
# RUN THE APP
# =========================
# Always base: this block starts the server
if __name__ == "__main__":
    app.run(debug=True)  # debug=True for development only