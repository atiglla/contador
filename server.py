from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key="lalalalala"

@app.route('/')
def index():
    if "contador" not in session:
        session["contador"] = 0
    else:
        session['contador'] += 1
    return render_template("index.html")

@app.route('/mas2')
def index2():
    if "contador" not in session:
        session["contador"] = 0
    else:
        session['contador'] += 2
    return render_template("index.html")

@app.route('/destroy_session/')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)