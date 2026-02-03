from flask import Flask, render_template
import requests as rq
import json
from pathlib import Path

# API for blogs
all_blogs_link = "https://api.npoint.io/4ef3129582a92084b09d"
# # Get all blog posts with api call => (commented because of Connection Aborted)
# all_blogs = rq.get(all_blogs_link, timeout=5).json()

# Get root folder, static and templates address
root_path = Path(__file__).resolve().parent
static_path = root_path/'static'
templates_path = root_path/'templates' 

# Read blog posts from JSON file instead of API call
with open(fr"{static_path}\blog-data.txt") as file:
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