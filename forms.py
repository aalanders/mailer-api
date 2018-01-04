from flask_wtf import Form
from wtforms import StringField, validators

class EmailForm(Form):
    to = StringField('To', [validators.Length(min=1, max=35)])
    subject = StringField('Subject', [validators.Length(min=1, max=35)])
    body = StringField('Message', [validators.Length(min=1, max=300)])