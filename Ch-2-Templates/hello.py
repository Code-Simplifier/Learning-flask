from flask import Flask, render_template
# from flask_bootstrap import Bootstrap

app = Flask(__name__)
# bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.errorhandler(404)
def error(e):
    return render_template('error.html'), 404

if __name__ == "__main__":
    app.run(debug=True)