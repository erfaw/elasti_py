from flask import Flask, render_template
import requests as rq


app = Flask(__name__)

@app.route('/')
def home():
    # Blogs api
    all_blogs_link = "https://api.npoint.io/4ef3129582a92084b09d"
    # Get all blog posts
    all_blogs = rq.get(all_blogs_link).json()
    return render_template("index.html", all_blogs=all_blogs)

if __name__ == "__main__":
    app.run(debug=True)
