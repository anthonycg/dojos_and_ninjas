# from crypt import methods
# from unicodedata import name
from unicodedata import name
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return render_template('dojo.html', all_dojos=Dojo.show())

@app.route('/create/dojo', methods=['POST'])
def dojo_create():
    data = {
        'name': request.form['name']
    }
    Dojo.save(data)
    return redirect('/')

@app.route('/show/ninjas/<int:id>')
def show_dojo_with_ninjas(id):
    data = {
        'id':id
    }
    print('ala')
    return render_template('show.html', dojo = Dojo.get_all_ninjas_in_dojo(data))


