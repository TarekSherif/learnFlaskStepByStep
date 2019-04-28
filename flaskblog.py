
from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# python
# import secrets
# secrets.token_hex(16)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
# from flaskblog import db
# db.create_all()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/hello")
def hello():
    return "<h1>Hello  html!</h1>"


@app.route("/test")
def test():
    res = """
    <html>
        <head><title>just test</title></head>
    """
    res += "<body>"

    for i in range(1, 7):
        res += f"<h{i}>test</h{i}>"

    res += """
    </body>
    </html>
    """
    return res


@app.route("/loadpage")
def loadpage():
    with open("test.html") as f:
        content = str().join(f.readlines())
        return content


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="about")


@app.route("/singup", methods=["GET", "POST"])
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created from {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template('Register.html', title="Register", form=form)


@app.route("/signin", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "Eng.tarek.sherif@gmail.com" and form.password.data == "01115500920":
            flash(f"Account created from {form.email.data}!", "success")
            return redirect(url_for("home"))
        else:
            flash(f"login Unsuccessful , please check user name and password", "danger")

    return render_template('Login.html', title="Login", form=form)


    # To run Project "flask run"
    # by default flask will run app.py
    # if we wont to run  different file
    # Run for win set FLASK_APP=flaskblog.py
    # Run for linex export  FLASK_APP=flaskblog.py
    # OR
    # python FileName.py
    # =================================================================
    # debug=True  to update page without restart server
    # by default debug=false to change it
    # Run for win set FLASK_DEBUG=1
    # Run for linex export  FLASK_DEBUG=1
    # or
if __name__ == "__main__":
    app.run(debug=True)
