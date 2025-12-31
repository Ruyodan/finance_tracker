# finance_app.py
from flask import Flask

# Create the Flask app object
app = Flask(__name__)

# Define a route: when someone visits "/", run this function
@app.route("/")
def home():
    return "Welcome to Finance Tracker!"

# Run the app only if this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)