from flask import Flask, render_template, request, redirect, url_for
import utils.login
import utils.register

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    return render_template("login.html")

@app.route("/lauth", methods=["POST"])
def loginAuth():
    loginOutcome = utils.login.login(request.form['user'],request.form['pw'])
    if loginOutcome == 2:
        return redirect(url_for("main"), code=307)
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

@app.route("/main", methods=["POST"])
def main():
    return "You made it!"
   
if __name__ == "__main__":
    app.debug = True
    app.run()
