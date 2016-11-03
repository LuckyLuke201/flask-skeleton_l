"""
Logic for dashboard related routes
"""
from flask import Blueprint, render_template,url_for,request,redirect
from .forms import LogUserForm, DortForm
from ..data.database import db
from ..data.models import LogUser, DortDB
blueprint = Blueprint('public', __name__)

@blueprint.route('/', methods=['GET'])
def index():
    return render_template('public/index.tmpl')

@blueprint.route('/loguserinput',methods=['GET', 'POST'])
def InsertLogUser():
    form = LogUserForm()
    if form.validate_on_submit():
        LogUser.create(**form.data)
    return render_template("public/LogUser.tmpl", form=form)

@blueprint.route('/loguserlist',methods=['GET'])
def ListuserLog():
    pole = db.session.query(LogUser).all()
    return render_template("public/listuser.tmpl",data = pole)

@blueprint.route('/dort', methods=['GET', 'POST'])
def dorty():
    form = DortForm()
    if form.validate_on_submit():
        DortDB.create(**form.data)
    return render_template("public/dort.tmpl", form=form)

@blueprint.route('/vypisdort', methods=['GET'])
def vypis_dorty():
    pole = db.session.query(DortDB).all()
    return render_template("public/vypisdort.tmpl", data=pole)

@blueprint.route('/smazat_dort/<int:id>', methods=['GET'])
def smazat_dorty(id):
    pole = db.session.query(DortDB).filter_by(id = id).first()
    db.session.delete(pole)
    db.session.commit()
    return redirect(request.args.get("next")or url_for("public.vypis_dorty"))