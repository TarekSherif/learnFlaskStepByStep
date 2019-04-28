
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = "6726d7ba022f383e45a2b836e1b52074"
# python
# import secrets
# secrets.token_hex(16)


posts = [{"title": "My Updated Post", "content": "My first updated post!\r\n\r\nThis is exciting!", "user_id": 1}, {"title": "A Second Post", "content": "This is a post from a different user...", "user_id": 2}, {"title": "Top 5 Programming Lanaguages",
                                                                                                                                                                                                                    "content": "Te melius apeirian postulant cum, labitur admodum cu eos! Tollit equidem constituto ut has. Et per ponderum sadipscing, eu vero dolores recusabo nec! Eum quas epicuri at, eam albucius phaedrum ad, no eum probo fierent singulis. Dicat corrumpit definiebas id usu, in facete scripserit eam.\r\n\r\nVim ei exerci nusquam. Agam detraxit an quo? Quo et partem bonorum sensibus, mutat minimum est ad. In paulo essent signiferumque his, quaestio sadipscing theophrastus ad has. Ancillae appareat qualisque ei has, usu ne assum zril disputationi, sed at gloriatur persequeris.", "user_id": 1}]


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
