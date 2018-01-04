from flask import Flask, redirect, render_template, url_for
import os

app = Flask(__name__)

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/data')
def index():
    return "Hello this is the mailer!"

if os.environ.get('ENV') == 'production':
    debug = False
else:
    debug = True

if __name__ == "__main__":
    app.run(debug=debug,port=3000)