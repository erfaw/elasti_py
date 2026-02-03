from flask import Flask, render_template

# Build flask app
app = Flask(__name__)

# Root page
@app.route('/')
def home_page():
    return render_template(
        "index.html"
    )

# Run idiom
if __name__ == "__main__":
    app.run(debug= True)