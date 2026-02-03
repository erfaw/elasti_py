from flask import Flask, render_template
from flask import request 

# Build flask app
app = Flask(__name__)

# Root page
@app.route('/')
def home_page():
    return render_template(
        "index.html"
    )

@app.route('/login', methods=["POST"])
def recieve_data():
    if request.method == 'POST':
        first_name = request.form['firstName']
        password = request.form['password']
    return f"""
<h1>
    first name: {first_name}, password: {password}
</h1>
"""

# Run idiom
if __name__ == "__main__":
    app.run(debug= True)