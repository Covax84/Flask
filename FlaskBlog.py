# start with bash:
# cd FlaskBlog
# export FLASK_APP=flaskblog.py  - regular mode, any py-file changes require restart a server to take effect
# export FLASK_DEBUG=1  - run flask in debug mode (changes take effect by simple refresh)
# flask run  - to run server on localhost
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello World!\nThis is a Home Page, welcome!</h1>'  # got just a whitespace instead of \n


@app.route('/About')
@app.route('/about')
def about():
    return '<h1>This is About Page!\n</h1>'


if __name__ == '__main__':
    pass
