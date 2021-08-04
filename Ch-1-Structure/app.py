from flask import Flask # importing flask 


# app is an instance of class 'Flask'
app = Flask(__name__)

# routes and view functions
@app.route('/')
def index():
    return 'Hello World'


# server setup
if __name__ == "__main__":
    app.run(debug=True)