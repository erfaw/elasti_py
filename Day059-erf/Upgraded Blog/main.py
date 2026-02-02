from flask import Flask, render_template

# Build flask app
app = Flask(__name__)

# Root home page
@app.route('/')
def home_page():
    return render_template(
        "index.html",
    )

# About page
@app.route('/about')
def about_page():
    return render_template(
        "about.html"
    )

# Contact page
@app.route('/home')
def contact_page():
    return render_template(
        "contact.html"
    )

# Idiom run
if __name__ == "__main__":
    app.run(debug= True)