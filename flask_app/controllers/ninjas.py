from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninja')
def ninja():
    return render_template('ninjas.html', all_dojos = Dojo.show())

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    print(request.form['dojo_id'])
    data = {
        'dojo_id': request.form['dojo_id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    Ninja.save(data)
    return redirect('/')

# @app.route('/show/ninjas/<int:id>')
# def show_ninjas(id):
#     data = {
#         'id':id
#     }
#     all_ninjas = Ninja.show(data)
#     return render_template('show.html', all_ninjas=all_ninjas)
