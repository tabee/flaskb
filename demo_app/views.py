from flask import render_template, request, redirect, url_for, flash

from demo_app import app
from demo_app.logikmodule import User


name_app = app.config.get('APPLICATION_NAME')
user = User()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        user.setname(request.form['username'])
        user.setpw(request.form['password'])
        if user.checklogin(user.name, user.password):
            error = 'success'
            flash('You were successfully logged in')
        else:
            error = 'warning'
            flash('Warning! Better check yourself, you')
    else:
        error = 'info'
        flash('Well done! You successfully read this important alert message.')
    return render_template('index.html', app_name=name_app, username=user.name, password=user.password, error=error)

@app.route('/secret')
def secret():
    if not user.checklogin(user.name, user.password):
        error = 'warning'
        flash('Error! Better check yourself, you')
        user.destroy()
        return redirect(url_for('index', error=error))
    return render_template('page-secret.html', app_name=name_app)

@app.route('/killsession')
def killsession():
    user.destroy()
    return redirect(url_for('index'))