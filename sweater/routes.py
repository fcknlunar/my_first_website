from datetime import datetime
from flask import render_template, redirect, url_for, request, Flask, flash
from sweater import db, app
from sweater.models import User
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user


@app.route('/')
@app.route('/home')
@app.route('/main')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/faqs')
def faqs():
    return render_template('faqs.html')


@app.route('/aboutwebsite')
def about_website():
    return render_template('aboutwebsite.html')


@app.route('/404')
def error404():
    return render_template('404.html')


@app.route('/login', methods=['POST', 'GET'])
def login_page():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')

        if login and password:
            user = User.query.filter_by(login=login).first()

            if user and check_password_hash(user.password, password):
                login_user(user)

                #next_page = request.args.get('next')

                return redirect('/')
            else:
                flash('Login or password is not correct')
        else:
            flash('Please fill login and password fields')
            return render_template('login.html')
        return render_template('login.html')
    else:
        return render_template('login.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect('/login' + '?next=' + request.url)

    return response


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    login = request.form.get('login')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    regdate = datetime.utcnow()
    if request.method == 'POST':
        if not(login or password or password2):
            flash('Please, fill all fields!')
        elif password != password2:
            flash('Password are not equal!')
        else:
            hash_pwd = generate_password_hash(password)
            new_user = User(login=login, password=hash_pwd)
            db.session.add(new_user)
            db.session.commit()

            return redirect('/login')
    else:
        return render_template('signup.html')