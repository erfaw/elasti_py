from flask import Flask
app = Flask(__name__)

# Decorator: add bold element
def make_bold(f):
    def wrap_f():
        return '<b>'+ f() + '<b/>'
    return wrap_f

# Decorator: add emphasis element
def make_emphasis(f):
    def wrap_f():
        return '<em>'+ f() + '<em/>'
    return wrap_f

# Decorator: add underline element
def make_underline(f):
    def wrap_f():
        return '<u>' + f() + '<u/>'
    return wrap_f

@app.route('/')
def hello_world():
    return '<a style="color:red; border: 1px solid white; font-size: 50px;">Hello, World!<a/>'

@app.route('/<user_name>')
def greet(user_name):
    return f"salam {user_name} kesafat :) 😂"

@app.route('/gorba')
def kitty_page():
    return f'<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHVnw4nOFCGn_AR91QwGxE8vQEimLGNkopgA&s"/>'

@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
def bye():
    return 'Bye'

if __name__ == "__main__":
    app.run(debug= True)