from flask import Flask, render_template # type: ignore

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# About Page
@app.route("/about")
def about():
    return render_template("about.html")

# Services Page
@app.route("/services")
def services():
    return render_template("services.html")

# Gallery Page
@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

# Contact Page
@app.route("/contact")
def contact():
    return render_template("contact.html")
   

# Login Page
@app.route("/login")
def login():
    return render_template("login.html")

# Registration Page
@app.route("/register")
def register():
    return render_template("register.html")

# Run the application
if __name__ == "__main__":
    app.run(debug=True)