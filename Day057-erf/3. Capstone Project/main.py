from flask import Flask, render_template, url_for
import requests as rq

# Blogs api
all_blogs_link = "https://api.npoint.io/4ef3129582a92084b09d"
# Get all blog posts
all_blogs = rq.get(all_blogs_link).json()

# Build Flask app
app = Flask(__name__)

# Build root page
@app.route('/')
def home():
    return render_template("index.html", all_blogs=all_blogs)

# Build a post page for a blog id
@app.route('/post/<int:blog_id>')
def post(blog_id):

    # Gather specific blog post before rendering
    for blog in all_blogs:
        if blog_id == blog['id']:
            blog_to_render = blog

    return render_template(
        "post.html",
        # Send specific blog to render
        blog_to_render=blog_to_render,
    )

if __name__ == "__main__":
    app.run(debug=True)
