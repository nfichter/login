from flask import Flask, render_template, request, redirect, url_for, session
import utils.login
import utils.register

app = Flask(__name__)
app.secret_key = "PUT_SECRET_KEY_HERE" #to be changed but not pushed

#main page - if user is logged in, show the main page, otherwise show login/register page
@app.route("/")
def welcome():
    if 'username' in session:
        return render_template("index.html",loggedin=1,username=session['username'])
    return render_template("index.html",loggedin=0,username="none")

#gives the user a form to log in
@app.route("/login", methods=["POST"])
def login():
    redir = False #if redirected from the register page (Submit button was named Register instead of Login) then show a success message
    if request.form['Submit'] == "Register":
        redir = True
    return render_template("login.html",redirected = redir)

#checks if the username/password is incorrect (if not, logs the user in and redirects them to their updated main page)
@app.route("/lauth", methods=["POST"])
def loginAuth():
    loginOutcome = utils.login.login(request.form['user'],request.form['pw'])
    if loginOutcome == 2:
        session['username'] = request.form['user']
        return redirect("/")
    else:
        return render_template("lauth.html",outcome=loginOutcome)

#gives the user a form to register
@app.route("/register", methods=["POST"])
def register():
    return render_template("register.html")

#checks if the username exists (if not, registers the user and brings them to the login page)
@app.route("/rauth", methods=["POST"])
def registerAuth():
   if utils.register.register(request.form['user'],request.form['pw']):
       return redirect(url_for("login"), code=307) #code=307 allows the user to be redirected with the POST method
   else:
       return render_template("rauth.html")

#logs the user out by removing the username key from their session
@app.route("/logout", methods=["POST"])
def logout():
    session.pop('username')
    return redirect("/")

if __name__ == "__main__":
    app.debug = True
    app.run()
