import re

from flask_wtf import Form
from wtforms.fields import BooleanField, TextField, PasswordField, DateTimeField, IntegerField
from wtforms.validators import EqualTo, Email, InputRequired, Length

from ..data.models import User, LogUser
from ..fields import Predicate


def email_is_available(email):
    if not email:
        return True
    return not User.find_by_email(email)


def username_is_available(username):
    if not username:
        return True
    return not User.find_by_username(username)


def safe_characters(s):
    " Only letters (a-z) and  numbers are allowed for usernames and passwords. Based off Google username validator "
    if not s:
        return True
    return re.match(r'^[\w]+$', s) is not None


class LogUserForm(Form):
    jmeno = TextField('Choose your username', validators=[
        Predicate(safe_characters, message="Please use only letters (a-z) and numbers"),
        Length(min=6, max=30, message="Please use between 6 and 30 characters"),
        InputRequired(message="You can't leave this empty")
    ])
    prijmeni = TextField('Choose your username', validators=[
        Predicate(safe_characters, message="Please use only letters (a-z) and numbers"),
        Length(min=6, max=30, message="Please use between 6 and 30 characters"),
        InputRequired(message="You can't leave this empty")
    ])
    pohlavi = BooleanField('Pohlavi')


class DortForm(Form):
    DruhDortu = TextField('Druh dortu', validators=[
        Predicate(safe_characters, message="Pouze A-Z"),
        Length(min=3, max=25, message="Zadej nazev, 3 - 25"),
        InputRequired(message="Zadej aspon neco")
    ])
    Cena =  TextField('Cena', validators=[
            Predicate(safe_characters, message="Pouze cisla"),
            Length(min=2, max=3, message="Musis zadat aspon 2 cisla"),
            InputRequired(message="Zadej aspon neco")
    ])
