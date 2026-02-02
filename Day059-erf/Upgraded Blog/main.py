from flask import Flask, render_template
import requests as rq
import json

# API for blogs
all_blogs_link = "https://api.npoint.io/4ef3129582a92084b09d"
# Get all blog posts
# all_blogs = rq.get(all_blogs_link, timeout=5).json()
with open(r"G:\myDocuments\Programming\Python\elasti_py\Day059-erf\Upgraded Blog\static\blog-data.txt") as file:
    all_blogs = json.load(file)

# Build flask app
app = Flask(__name__)

# Root home page
@app.route('/')
def home_page():
    return render_template(
        "index.html",
        all_blogs=all_blogs
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