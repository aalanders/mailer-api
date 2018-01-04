from flask import Flask, redirect, render_template, url_for, request
from forms import EmailForm
import os

app = Flask(__name__)

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/data', methods=['GET','POST'])
def index():
    form = EmailForm(request.form, csrf_enabled=False)
    if request.method == 'POST':
        if form.validate():
            flash('Your email message has been sent!')
            return redirect(url_for('index'))

    return render_template('index.html', form=form)

if os.environ.get('ENV') == 'production':
    debug = False
else:
    debug = True

if __name__ == "__main__":
    app.run(debug=debug,port=3000)