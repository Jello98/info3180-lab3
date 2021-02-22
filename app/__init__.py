from flask import Flask
from flask_mail import Mail
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)


app.config['SECRET_KEY'] = 'thefadergang'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USERNAME'] = '5ff422587a9066'
app.config['MAIL_PASSWORD'] = 'bdfb005adf4fd7'


mail = Mail(app)
from app import views