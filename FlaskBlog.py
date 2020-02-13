# start with bash:
# cd FlaskBlog
# export FLASK_APP=flaskblog.py  - regular mode, any py-file changes require restart a server to take effect
# export FLASK_DEBUG=1  - run flask in debug mode (changes take effect by simple refresh)
# flask run  - to run server on localhost
# python flaskblog.by  - same as flask run
from flask import Flask, render_template

app = Flask(__name__)

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
def hello():
    return render_template('home.html', posts=posts, title='Homepage')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
