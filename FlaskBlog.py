# start with bash:
# cd FlaskBlog
# export FLASK_APP=flaskblog.py  - regular mode, any py-file changes require restart a server to take effect
# export FLASK_DEBUG=1  - run flask in debug mode (changes take effect by simple refresh)
# flask run  - to run server on localhost
# python flaskblog.by  - same as flask run
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '4f42ae8ecfa6c037c633728707169dac'

posts = [
    {
        'author': 'Covax84',
        'title': 'Blog post 1',
        'content': 'Contents of very first post',
        'date_posted': '13 february 2020'
    },
    {
        'author': 'Afon',
        'title': 'Blog post 2',
        'content': 'Contents of second post',
        'date_posted': '13 february 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='Homepage')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created For {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
