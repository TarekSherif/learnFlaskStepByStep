
from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm

from flaskblog.models import User, Post


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
