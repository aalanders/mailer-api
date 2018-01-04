from flask import Flask, redirect, render_template, url_for, request, flash, jsonify
from forms import EmailForm
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SENDER_EMAIL'] = os.environ.get('SENDER_EMAIL')
app.config['SENDER_PASSWORD'] = os.environ.get('SENDER_PASSWORD')
app.config.update(
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = app.config['SENDER_EMAIL'],
	MAIL_PASSWORD = app.config['SENDER_PASSWORD']
)
mail = Mail(app)

@app.route('/', methods=['GET','POST'])
def index():
    form = EmailForm(request.form, csrf_enabled=False)
    if request.method == 'POST':
        if form.validate():
            try: 
                ##if form validates, send email, return success
                msg = Message(form.subject.data, sender=MAIL_USERNAME, recipients=[form.to.data])
                msg.body = form.body.data
                mail.send(msg)
                flash('Your email message has been sent!')
                return jsonify({'Success': 1})
            except Exception as inst:
                return(str(inst))
        else:
            return jsonify({'Failure': 0})

    return render_template('index.html', form=form)

if os.environ.get('ENV') == 'production':
    debug = False
else:
    debug = True

if __name__ == "__main__":
    app.run(debug=debug,port=3000)