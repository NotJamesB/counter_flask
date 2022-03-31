from unicodedata import name
from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key="James"

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    else:
        session['count'] += 1
    return render_template("counter.html")

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect("/")

@app.route('/2')
def plus2():
    session['count'] += 1
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)