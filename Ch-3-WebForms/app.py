from flask import Flask, render_template
from forms import NameForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ILovePython$$FlaskIsGood^&223366'

@app.route('/', methods=['GET', 'POST'])
def home():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('home.html', form=form, name=name)

if __name__ == "__main__":
    app.run(debug=True)