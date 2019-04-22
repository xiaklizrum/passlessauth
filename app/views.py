import uuid
from app import app, session
from datetime import datetime, timedelta
from flask import render_template, request
from .api import Email
from .creditals import EMAIL_FROM
from .forms import RequestForm
from .models import User, SignInRequest


@app.route('/', methods=['GET', 'POST'])
def login():
    form = RequestForm()
    if form.validate_on_submit():
        user = session.query(User).filter_by(email=form.email.data).first()
        if user:
            return render_template(
                'auth.html',
                result='User with email {} already exist'.format(
                    form.email.data)
            )
        user = User(email=form.email.data)
        session.add(user)
        invoice = SignInRequest(
            email=form.email.data,
            token=str(uuid.uuid4()),
            ip=request.remote_addr,
            expired=datetime.now() + timedelta(days=30)
        )
        session.add(invoice)
        sender = Email()
        sender.send(
            EMAIL_FROM,
            invoice.email,
            'ACTIVATION',
            '<a>http://127.0.0.1:5000/invoice/{}</a>'.format(invoice.token)
        )
        session.commit()
        return render_template(
            'auth.html',
            result='Get auth link on {}'.format(form.email.data)
        )
    return render_template('index.html', form=form)


@app.route('/invoice/<hash>')
def activate(hash):
    invoice = session.query(SignInRequest).filter_by(
        token=hash, activated=False).first()
    if invoice:
        invoice.activated = datetime.now()
        session.add(invoice)
        session.commit()
        reason = 'success'
    else:
        reason = 'failed'
    return render_template('auth.html', result=reason)
