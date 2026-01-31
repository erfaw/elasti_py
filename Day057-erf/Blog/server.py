from flask import Flask

# Build Flask app
app = Flask(__name__)

# Build root page
@app.route('/')
def home():
    pass

# Run server
if __name__ == "__name__":
    app.run(debug= True)