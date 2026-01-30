from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<a style="color:red; border: 1px solid white; font-size: 50px;">Hello, World!<a/>'

@app.route('/<user_name>')
def greet(user_name):
    return f"salam {user_name} kesafat :) 😂"

if __name__ == "__main__":
    app.run(debug= True)