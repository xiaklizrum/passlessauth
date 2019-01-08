from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import Required


class CSRFProtectForm(FlaskForm):
    class Meta:
        csrf = False


class RequestForm(CSRFProtectForm):
    email = TextField('email', validators=[Required()])
