from flask import Flask, render_template
import requests as rq
root_url = "http://127.0.0.1:5000"

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

# Build all blogs page
blogs_url = r"blogs"
@app.route(f'/{blogs_url}')
def blogs():
    return render_template("all_blogs.html", all_blogs=all_blogs, root_url=root_url, blogs_url=blogs_url)

# Build each blog post page
@app.route(f'/{blogs_url}/<int:post_id>')
def blog_post(post_id):
    return render_template("single_blog.html", all_blogs=all_blogs, post_id=post_id)

# Run server
if __name__ == "__main__":
    app.run(debug= True)