from flask import Flask, render_template, request, redirect, url_for, session
import utils.login
import utils.register

app = Flask(__name__)
app.secret_key = "1mansdfLWER1q2nzs=z[234;werw]11111vvvbaq3we"

@app.route("/")
def welcome():
    if 'username' in session:
        return render_template("index.html",loggedin=1,username=session['username'])
    return render_template("index.html",loggedin=0,username="none")

@app.route("/login", methods=["POST"])
def login():
    redir = False
    for key in request.form:
        print key, request.form[key]
    if request.form['Submit'] == "Register":
        redir = True
    return render_template("login.html",redirected = redir)

@app.route("/lauth", methods=["POST"])
def loginAuth():
    loginOutcome = utils.login.login(request.form['user'],request.form['pw'])
    if loginOutcome == 2:
        session['username'] = request.form['user']
        return redirect("/")
    else:
        return render_template("lauth.html",outcome=loginOutcome)

@app.route("/register", methods=["POST"])
def register():
    return render_template("register.html")

@app.route("/rauth", methods=["POST"])
def registerAuth():
   if utils.register.register(request.form['user'],request.form['pw']):
       return redirect(url_for("login"), code=307)
   else:
       return render_template("rauth.html")

@app.route("/logout", methods=["POST"])
def logout():
    session.pop('username')
    return redirect("/")

if __name__ == "__main__":
    app.debug = True
    app.run()
