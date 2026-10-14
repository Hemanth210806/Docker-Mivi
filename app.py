
from flask import Flask, jsonify, render_template
import os

# Get the directory where app.py is located
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Initialize Flask with explicit template and static folders
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)


# Router 1: Home Page
@app.get("/")
def home():
    return render_template("index.html")


# Router 2: Health Page
@app.get("/health")
def health():
    return render_template("health.html")


# API: Health Check
@app.get("/api/health")
def health_api():
    return jsonify(
        status="ok",
        application="Mevi Flask Demo"
    )


# Router 3: Greeting Page
@app.get("/greet")
def greet_page():
    return render_template("greet.html")


# API: Personalized Greeting
@app.get("/api/greet/<name>")
def greet_api(name):
    return jsonify(
        message=f"Hello, {name}!"
    )


# Router 4: About Page
@app.get("/about")
def about():
    return render_template("about.html")


# Router 5: Contact Page
@app.get("/contact")
def contact():
    return render_template("contact.html")


# Run the Flask application
if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5001,
        debug=True
    )
