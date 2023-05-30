from flask import render_template, redirect, url_for, request, Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(16), nullable=False)
    password = db.Column(db.String(16), nullable=False)
    regdate = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Users %r>' % self.id


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


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        regdate = datetime.utcnow()
        usr = User(email=email, password=password, regdate=regdate)

        try:
            db.session.add(usr)
            db.session.commit()
            return render_template('successsignup.html')
        except:
            return redirect('/404')

    else:
        return render_template('signup.html')


@app.route('/aboutwebsite')
def about_website():
    return render_template('aboutwebsite.html')


@app.route('/404')
def error404():
    return render_template('404.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        return redirect('/404')
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)