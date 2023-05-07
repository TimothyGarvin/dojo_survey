from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'heresyTDS'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/return', methods =['POST'])
def return_user():
    session['name'] = request.form['name']
    session['dojoLocation'] = request.form['dojoLocation']
    session['favoriteLanguage'] = request.form['favoriteLanguage']
    session['comment'] = request.form['comment']
    print(request.form)
    return redirect('/user')

@app.route('/user')
def return_page():
    print(session)
    return render_template("return.html")

if __name__=="__main__":
    app.run(debug=True)