from flask import Flask, escape, url_for

app = Flask(__name__)

@app.route('/home')
def hello():
    return u'欢迎来到我的WatchList!'

@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % escape(name)

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name='greyli'))
    print(url_for('user_page', name='peter'))
    print(url_for('test_url_for', num=2))
    return 'Test Page'

