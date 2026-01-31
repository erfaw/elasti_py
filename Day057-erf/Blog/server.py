from flask import Flask, render_template
import requests as rq

# blogs api
all_blogs_link = "https://api.npoint.io/4ef3129582a92084b09d"

# Get all blog posts
all_blogs = rq.get(all_blogs_link).json()

# Build Flask app
app = Flask(__name__)

# Build root page
@app.route('/')
def home_page():
    return render_template('home_page.html', blogs_url=blogs_url)

# Build blogs page
blogs_url = r"blogs"
@app.route(f'/{blogs_url}')
def blogs():
    return render_template("blog_template.html", all_blogs=all_blogs)

# Run server
if __name__ == "__main__":
    app.run(debug= True)