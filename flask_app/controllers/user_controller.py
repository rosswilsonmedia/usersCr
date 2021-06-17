from flask import render_template, request, redirect

from flask_app import app
from ..models.user import User

@app.route('/users')
def user():
    users = User.get_all()
    print(users)
    return render_template('users.html', all_users=users)

@app.route('/users/new')
def new_user():
    return render_template('new_user.html')

@app.route('/users/save', methods=['POST'])
def save_new_user():
    data={
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email']
    }
    User.save(data)
    return redirect('/users')
