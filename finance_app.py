# Always import Flask and other helpers you need
from flask import Flask, render_template, request

# Always create the app object like this
app = Flask(__name__)

# =========================
# Route: Homepage
# =========================
# @app.route("/") → always the same pattern for defining routes
# def home(): → function name can change, but must return something
@app.route("/")
def home():
    # Always use render_template to load HTML files from /templates
    return render_template("home.html")

# =========================
# Route: Handle Form Submission
# =========================
# @app.route("/add", methods=["POST"]) → pattern always the same when handling form POST requests
@app.route("/add", methods=["POST"])
def add_transaction():
    # request.form[...] → always used to get values from submitted form
    amount = request.form["amount"]        # custom field name (matches HTML form)
    t_type = request.form["type"]          # custom field name (matches HTML form)
    description = request.form["description"]  # custom field name (matches HTML form)

    # For now, just return a confirmation message
    # This part is customizable: later we’ll save to database instead
    return f"Added {t_type}: {amount} ({description})"

# =========================
# Run the App
# =========================
# Always use this block to start the server
if __name__ == "__main__":
    app.run(debug=True)