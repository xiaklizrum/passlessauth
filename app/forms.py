from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class CSRFProtectForm(FlaskForm):
    class Meta:
        csrf = False


class RequestForm(CSRFProtectForm):
    email = StringField('email', validators=[DataRequired()])
