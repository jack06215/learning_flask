from flask import Flask, url_for, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/hello')
def hello_world():
    return 'Hello World'


@app.route('/')
def index():
    return render_template('index.html', message='Jack')


@app.route('/user/<username>')
def show_user_profile(username):
    return 'Username: {}'.format(str(username))


@app.route('/post/<post_id>')
def show_post(post_id):
    return 'Post{}'.format(str(post_id))


app.run(port=8100, debug=True)